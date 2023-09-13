using Amazon.DynamoDBv2.DataModel;

namespace asp_dotnet_mac.Models;

// Focusing on the object persistence model to make it as seamless and integrated with the language as possible
// https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DotNetSDKHighLevel.html

[DynamoDBTable("InventoryTable")]
public class ExampleDataModel
{
    [DynamoDBHashKey]
    public string pk { get; set; }
    
    [DynamoDBRangeKey]
    public string sk { get; set; }
    
    [DynamoDBProperty]
    public EngineDimensions engineDimensions { get; set; }
    
    [DynamoDBProperty]
    public string make { get; set; }
    
    [DynamoDBProperty]
    public string model { get; set; }
    
    [DynamoDBProperty]
    public List<string> packages { get; set; }
}

public class EngineDimensions
{
    public decimal bore { get; set; }
    
    public decimal stroke { get; set; }
    
    public decimal displacement { get; set; }
    
    public int cylinders { get; set; }
    
    public int valves { get; set; }
}

// public class EngineDimensionsConverter : IPropertyConverter
// {
//     public DynamoDBEntry ToEntry(object value)
//     {
//         if (value is not EngineDimensions engineDimensions) throw new ArgumentOutOfRangeException();
//         
//         return ;
//     }
//
//     public object FromEntry(DynamoDBEntry entry)
//     {
//         throw new NotImplementedException();
//     }
// }

