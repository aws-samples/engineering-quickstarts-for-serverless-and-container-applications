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

@ExtendWith(SpringExtension.class)
@WebMvcTest(HelloWorldController.class)
public class HelloWorldControllerTest {
    @Autowired
    private MockMvc mockMvc;

    @MockBean
    private Application app;

    @Test
    public void getCart() throws Exception {
        mockMvc.perform(get("/getCart"))
                .andExpect(status().isOk());
    }

    @Test
    public void addToCart() throws Exception {

    }
}