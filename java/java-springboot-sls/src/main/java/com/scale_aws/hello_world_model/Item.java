package com.scale_aws.hello_world_model;

import software.amazon.awssdk.enhanced.dynamodb.mapper.annotations.*;

@DynamoDbBean
public class Item {
    private String pk;
    private String sk;

    @DynamoDbPartitionKey
    public String getPk() {
        return pk;
    }

    public void setPk(String pk) {
        this.pk = pk;
    }

    @DynamoDbSortKey
    public String getSk() {
        return sk;
    }

    public void setSk(String sk) {
        this.sk = sk;
    }
}
