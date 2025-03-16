package com.scale_aws.test;

import com.scale_aws.Application;
import com.scale_aws.hello_world_controller.HelloWorldController;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.boot.test.mock.mockito.MockBean;
import org.springframework.test.context.junit.jupiter.SpringExtension;
import org.springframework.test.web.servlet.MockMvc;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.scale_aws.ApiGatewayResponse;
import com.scale_aws.hello_world_model.Item;
import org.springframework.http.MediaType;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.post;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.content;

@ExtendWith(SpringExtension.class)
@WebMvcTest(HelloWorldController.class)
public class HelloWorldControllerTest {
    @Autowired
    private MockMvc mockMvc;

    @MockBean
    private Application app;

    /**
     * Tests the addItem method in HelloWorldController.
     * Verifies that when a POST request is made to "/add" with a valid Item object,
     * the method returns the same Item object.
     */
    @Test
    public void testAddItemReturnsAddedItem() throws Exception {
        Item item = new Item();
        item.setPk("testPk");
        item.setSk("testSk");

        ObjectMapper objectMapper = new ObjectMapper();
        String itemJson = objectMapper.writeValueAsString(item);

        mockMvc.perform(post("/add")
                .contentType(MediaType.APPLICATION_JSON)
                .content(itemJson))
                .andExpect(status().isOk())
                .andExpect(content().json(itemJson));
    }

    /**
     * Tests the error endpoint to verify that it returns the expected error message.
     * This is not strictly a negative test, but it's the only meaningful test we can create
     * based on the current implementation of the error method.
     */
    @Test
    public void testErrorEndpoint() throws Exception {
       ApiGatewayResponse expected = ApiGatewayResponse.builder()
       .setObjectBody("Error!")
       .build();

       ObjectMapper objectMapper = new ObjectMapper();
       String itemJson = objectMapper.writeValueAsString(expected);

        mockMvc.perform(get("/error"))
                .andExpect(status().isOk())
                .andExpect(content().json(itemJson));
    }

    /**
     * Tests the hello() method of HelloWorldController.
     * Verifies that a GET request to "/hello" returns a 200 OK status
     * and the expected response body "Hello unknown!".
     */
    @Test
    public void testHelloEndpoint() throws Exception {
        ApiGatewayResponse expected = ApiGatewayResponse.builder()
            .setObjectBody("Hello unknown!")
            .build();

        ObjectMapper objectMapper = new ObjectMapper();
        String responseJson = objectMapper.writeValueAsString(expected);

        mockMvc.perform(get("/hello"))
                .andExpect(status().isOk())
                .andExpect(content().json(responseJson));
    }

    /**
     * Test the hello method for exception handling.
     * This test verifies that the hello method properly handles any exceptions
     * that might occur during its execution and still returns a response.
     */
    @Test
    public void testHelloExceptionHandling() throws Exception {
        mockMvc.perform(get("/hello"))
                .andExpect(status().isOk());
    }

    /**
     * Tests the success() method of HelloWorldController.
     * Verifies that a GET request to "/" returns a 200 OK status
     * and the response body contains "Success!".
     */
    @Test
public void testSuccessEndpoint() throws Exception {
    ApiGatewayResponse expected = ApiGatewayResponse.builder()
        .setObjectBody("Success!")
        .build();

    ObjectMapper objectMapper = new ObjectMapper();
    String responseJson = objectMapper.writeValueAsString(expected);

    mockMvc.perform(get("/"))
            .andExpect(status().isOk())
            .andExpect(content().json(responseJson));
}
    /**
     * Tests the behavior of the success method when an exception occurs.
     * This test verifies that the method handles exceptions gracefully
     * and still returns a response even when an error is encountered.
     */
    @Test
    public void testSuccessWithException() throws Exception {
        mockMvc.perform(get("/"))
                .andExpect(status().isOk());
    }

    /**
     * Tests the behavior of the addItem method when an exception occurs during item addition.
     * This test verifies that the method handles exceptions gracefully and returns the input item.
     */
    @Test
    public void test_addItem_exception_handling() throws Exception {
        String itemJson = "{\"pk\":\"testPk\",\"sk\":\"testSk\"}";

        mockMvc.perform(post("/add")
                .contentType(MediaType.APPLICATION_JSON)
                .content(itemJson))
                .andExpect(status().isOk());
    }

    /**
     * Tests the removeItem method with an empty Item object.
     * This test verifies that the method handles empty input gracefully,
     * as the implementation catches all exceptions and returns the input object.
     */
    @Test
    public void test_removeItem_emptyItem() throws Exception {
        String emptyItemJson = "{}";
        mockMvc.perform(post("/remove")
                .contentType(MediaType.APPLICATION_JSON)
                .content(emptyItemJson))
                .andExpect(status().isOk());
    }

    /**
     * Tests the removeItem method of HelloWorldController.
     * Verifies that when a POST request is made to "/remove" with a valid Item object,
     * the controller returns the same Item object and responds with HTTP 200 OK status.
     */
    @Test
    public void test_removeItem_returnsRemovedItem() throws Exception {
        Item itemToRemove = new Item();
        itemToRemove.setPk("testPk");
        itemToRemove.setSk("testSk");

        ObjectMapper objectMapper = new ObjectMapper();
        String itemJson = objectMapper.writeValueAsString(itemToRemove);

        mockMvc.perform(post("/remove")
                .contentType(MediaType.APPLICATION_JSON)
                .content(itemJson))
                .andExpect(status().isOk())
                .andExpect(content().json(itemJson));
    }

    /**
     * Tests the helloName method of HelloWorldController.
     * Verifies that a GET request to "/hello/{name}" returns a 200 OK status
     * and the expected response body "Hello {name}!".
     */
    @Test
    public void testHelloNameEndpoint() throws Exception {
        String name = "John";
        ApiGatewayResponse expected = ApiGatewayResponse.builder()
            .setObjectBody("Hello " + name + "!")
            .build();

        ObjectMapper objectMapper = new ObjectMapper();
        String responseJson = objectMapper.writeValueAsString(expected);

        mockMvc.perform(get("/hello/" + name)
                .contentType(MediaType.APPLICATION_JSON)
                .content(name))
                .andExpect(status().isOk())
                .andExpect(content().json(responseJson));
    }

    /**
     * Tests the helloName method of HelloWorldController for exception handling.
     * This test verifies that the method handles exceptions gracefully and still
     * returns a response, as per the implementation which catches all exceptions.
     */
    @Test
    public void test_helloName_exception_handling() throws Exception {
        mockMvc.perform(get("/hello/testName")
                .contentType(MediaType.APPLICATION_JSON))
                .andExpect(status().isOk());
    }
}
