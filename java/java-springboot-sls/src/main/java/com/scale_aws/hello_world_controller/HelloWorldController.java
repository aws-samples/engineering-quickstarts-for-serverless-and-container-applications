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

@RestController
@EnableWebMvc
public class HelloWorldController {
    private static final Logger logger = LogManager.getLogger(HelloWorldController.class);

    private static final DynamoDbEnhancedClient dbClient = DynamoDbEnhancedClient.create();

    @RequestMapping(path = "/hello/<name>", method = RequestMethod.GET)
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

    @RequestMapping(path = "/hello", method = RequestMethod.GET)
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

    @RequestMapping(path = "/add", method = RequestMethod.POST)
    public Item addItem(@RequestBody Item toAdd) {
        logger.info("Serving /add");

        ApiGatewayResponse.Builder responder = ApiGatewayResponse.builder();

        try {
            DynamoDbTable<Item> table = dbClient.table(System.getenv("DYNAMO_TABLE"), TableSchema.fromBean(Item.class));

            table.putItem(toAdd);
        } catch (Exception e) {
            logger.info("Generic Exception, " + e);
        }

        return toAdd;
    }


    // Add a post request to remove an item from the database
    @RequestMapping(path = "/remove", method = RequestMethod.POST)
    public Item removeItem(@RequestBody Item toRemove) {
        logger.info("Serving /remove");

        ApiGatewayResponse.Builder responder = ApiGatewayResponse.builder();

        try {
            DynamoDbTable<Item> table = dbClient.table(System.getenv("DYNAMO_TABLE"), TableSchema.fromBean(Item.class));

            table.deleteItem(r -> r.key(k -> k.partitionValue(toRemove.getPk()).sortValue(toRemove.getSk())));

        } catch (Exception e) {
            logger.info("Generic Exception, " + e);
        }

        return toRemove;
    }

    @RequestMapping(path = "/error", method = RequestMethod.GET)
    public ApiGatewayResponse error() {
        logger.info("Serving /error");

        ApiGatewayResponse.Builder responder = ApiGatewayResponse.builder();

        try {
            responder.setObjectBody("Error!");
        } catch (Exception e) {
            logger.info("Generic Exception, " + e);
        }

        return responder.build();
    }

    @RequestMapping(path = "/", method = RequestMethod.GET)
    public ApiGatewayResponse success() {
        logger.info("Serving /");

        ApiGatewayResponse.Builder responder = ApiGatewayResponse.builder();

        try {
            responder.setObjectBody("Success!");

            return responder.build();
        } catch (Exception e) {
            logger.info("Generic Exception, " + e);
        }

        return responder.build();
    }
}
