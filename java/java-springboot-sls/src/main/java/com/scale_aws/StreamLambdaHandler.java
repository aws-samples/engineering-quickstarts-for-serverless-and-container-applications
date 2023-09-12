package com.scale_aws;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.serverless.proxy.model.AwsProxyResponse;
import com.amazonaws.serverless.proxy.internal.testutils.Timer;
import com.amazonaws.serverless.proxy.model.HttpApiV2ProxyRequest;
import com.amazonaws.services.lambda.runtime.RequestStreamHandler;
import com.amazonaws.serverless.exceptions.ContainerInitializationException;
import com.amazonaws.serverless.proxy.spring.SpringBootLambdaContainerHandler;

import io.opentelemetry.api.GlobalOpenTelemetry;
import io.opentelemetry.api.common.AttributeKey;
import io.opentelemetry.api.common.Attributes;
import io.opentelemetry.api.metrics.LongUpDownCounter;
import io.opentelemetry.api.metrics.Meter;

import org.apache.logging.log4j.Logger;
import org.apache.logging.log4j.LogManager;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;

public class StreamLambdaHandler implements RequestStreamHandler {
    private static final SpringBootLambdaContainerHandler<HttpApiV2ProxyRequest, AwsProxyResponse> handler;
    private static final Logger logger;

    static {
        try {
            handler = SpringBootLambdaContainerHandler.getHttpApiV2ProxyHandler(Application.class);
            logger = LogManager.getLogger(Application.class);

        } catch (ContainerInitializationException e) {
            e.printStackTrace();

            throw new RuntimeException("Could not initialize Spring Boot application", e);
        }
    }

    public StreamLambdaHandler() {
        // enable the timer for debugging. Don't enable in production.
//        Timer.enable();
    }

    @Override
    public void handleRequest(InputStream inputStream, OutputStream outputStream, Context context) throws IOException {
        logger.info("Entered Request Handler, " + inputStream.toString() + " with Context, " + context.toString());
        handler.proxyStream(inputStream, outputStream, context);
    }
}
