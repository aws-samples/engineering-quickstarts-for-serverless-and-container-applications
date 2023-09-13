using System.Collections;
using Amazon.DynamoDBv2;
using Amazon.DynamoDBv2.DataModel;
using Amazon.Runtime;
using Microsoft.AspNetCore.Mvc;
using asp_dotnet_mac.Models;

namespace asp_dotnet_mac.Controllers
{
    [ApiController]
    [Route("/ddb/")]
    public class DDbController : Controller
    {
        // Static might make it persist across invocations preventing multiple clients per function
        private static AWSCredentials _credentials = new EnvironmentVariablesAWSCredentials();
        private static AmazonDynamoDBClient _client = new AmazonDynamoDBClient(_credentials);

        [HttpGet("get")]
        public IEnumerable<ExampleDataModel> GetAllVehicles()
        {

            return Array.Empty<ExampleDataModel>();
        }

        [HttpPost("get")]
        public IEnumerable<ExampleDataModel> GetVehicles(string query)
        {
            return Array.Empty<ExampleDataModel>();
        }

        [HttpGet("addDefault")]
        public IActionResult AddDefaultVehicle()
        {
            var context = new DynamoDBContext(_client);

            // Dummy car, testing how C# serializes info to JSON
            var engine = new EngineDimensions
            {
                bore=102m,
                stroke=81.5m,
                displacement=3996m,
                cylinders=6,
                valves=24
            };
            var packages = new List<string>
            {
                "Aero Package",
                "Weissach Package",
                "Racing Buckets",
                "Silver Deviated Stitching",
                "Silver Racing Harness",
                "Paint Match - Hermes Silver Band",
                "Bronze Lightweight Racing Alloys",
                "Pirelli P Zero - Racing Slicks"
            };
            var vehicle = new ExampleDataModel
            {
                pk = "992.1",
                sk = "190836193469",
                engineDimensions = engine,
                make = "Porsche",
                model = "911 GT3 RS",
                packages = packages
            };

            try
            {
                context.SaveAsync(vehicle).GetAwaiter().GetResult();
            }
            catch (Exception e)
            {
                return new UnprocessableEntityResult();
            }

            return new OkResult();
        }

        [HttpPost("add")]
        public IActionResult AddVehicles(ExampleDataModel toAdd)
        {
            // Every context might need to be different, might change this to be inside each api
            var context = new DynamoDBContext(_client);
            try
            {
                // Saved
                context.SaveAsync(toAdd).GetAwaiter().GetResult();
            }
            catch (Exception e)
            {
                return new UnprocessableEntityResult();
            }
            return new OkResult();
        }
        
        [HttpPost("update")]
        public IActionResult UpdateVehicles(ExampleDataModel toUpdate)
        {
            return new AcceptedResult();
        }

        [HttpPost("delete")]
        public IActionResult DeleteVehicles(ExampleDataModel toDelete)
        {
            return new AcceptedResult();
        }
    }
}

