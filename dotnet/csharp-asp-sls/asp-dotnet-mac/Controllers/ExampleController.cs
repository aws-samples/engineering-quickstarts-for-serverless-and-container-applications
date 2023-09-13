using Microsoft.AspNetCore.Mvc;
using AWS.Lambda.Powertools.Logging;
using AWS.Lambda.Powertools.Metrics;
using AWS.Lambda.Powertools.Tracing;

namespace asp_dotnet_mac.Controllers;

[ApiController]
[Route("/hello/")]
public class ExampleController : ControllerBase
{
    // Default controller
    [HttpGet]
    [Logging(LogEvent = true)]
    [Tracing(CaptureMode = TracingCaptureMode.ResponseAndError)]
    public string GetAnonHello()
    {
        Logger.LogInformation("Welcoming a stranger");
        return "Hello World, Anonymous!";
    }

    [HttpGet("{name}")]
    [Logging(LogEvent = true)]
    [Tracing(CaptureMode = TracingCaptureMode.ResponseAndError)]
    //[Metrics(CaptureColdStart = true)]
    public string GetPersonHello(string name)
    {
        Logger.LogInformation("Welcoming a known user, " + name);
        return "Hello " + name + ". Nice to see you!";
    }
}

