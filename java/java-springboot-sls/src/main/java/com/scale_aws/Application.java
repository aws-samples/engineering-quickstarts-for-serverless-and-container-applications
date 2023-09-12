package com.scale_aws;

import com.scale_aws.hello_world_controller.HelloWorldController;
import org.springframework.boot.SpringApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Import;
import org.springframework.web.servlet.HandlerAdapter;
import org.springframework.web.servlet.HandlerMapping;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.servlet.mvc.method.annotation.RequestMappingHandlerAdapter;
import org.springframework.web.servlet.mvc.method.annotation.RequestMappingHandlerMapping;

@SpringBootApplication
@Import({ HelloWorldController.class })
public class Application {

    @Bean
    public HandlerMapping handlerMapping() {
        return new RequestMappingHandlerMapping();
    }

    @Bean
    public HandlerAdapter handlerAdapter() {
        return new RequestMappingHandlerAdapter();
    }

    public static void main(String ... args) {
        SpringApplication.run(Application.class, args);
    }
}
