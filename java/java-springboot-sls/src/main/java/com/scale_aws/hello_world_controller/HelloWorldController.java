package com.scale_aws.hello_world_controller;

import com.scale_aws.hello_world_model.Item;
import org.apache.logging.log4j.Logger;
import com.scale_aws.ApiGatewayResponse;
import org.apache.logging.log4j.LogManager;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.config.annotation.EnableWebMvc;

import software.amazon.awssdk.enhanced.dynamodb.*;
import software.amazon.awssdk.enhanced.dynamodb.model.QueryConditional;
import software.amazon.awssdk.services.dynamodb.model.DynamoDbException;

import java.util.*;

@RestController
@EnableWebMvc
public class HelloWorldController {
    private static final Logger logger = LogManager.getLogger(HelloWorldController.class);

    private static final DynamoDbEnhancedClient dbClient = DynamoDbEnhancedClient.create();

    @RequestMapping(path="/hello/<name>", method=RequestMethod.GET)
    public ApiGatewayResponse helloName(@RequestBody String name) {
        logger.info("Serving /hello");

        ApiGatewayResponse.Builder responder = ApiGatewayResponse.builder();

        try {
            responder.setObjectBody("Hello " + name + "!");
        } catch (Exception e) {
            logger.info("Generic Exception, " + e);
        }

        return responder.build();
    }

    @RequestMapping(path="/hello", method=RequestMethod.GET)
    public ApiGatewayResponse hello() {
        logger.info("Serving /hello");

        ApiGatewayResponse.Builder responder = ApiGatewayResponse.builder();

        try {
            responder.setObjectBody("Hello unknown!");
        } catch (Exception e) {
            logger.info("Generic Exception, " + e);
        }

        return responder.build();
    }

    @RequestMapping(path="/add", method=RequestMethod.POST)
    public Item addItem(@RequestBody Item toAdd) {
        logger.info("Serving /add");

        ApiGatewayResponse.Builder responder = ApiGatewayResponse.builder();

        try {
            DynamoDbTable<Item> table = dbClient.table(System.getenv("DYNAMO_TABLE"), TableSchema.fromBean(Item.class));
            String pk = String.format("cart#%s", userId );

            QueryConditional query = QueryConditional.keyEqualTo(Key.builder().partitionValue(pk).build());

            cart = new ArrayList(Collections.singleton(table.query(r -> r.queryConditional(query)).items().iterator()));
            responder.setObjectBody(cart);
        } catch (Exception e) {
            logger.info("Generic Exception, " + e);
        }
    }

    @RequestMapping(path="/", method=)
}
