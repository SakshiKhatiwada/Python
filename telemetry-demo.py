from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor, ConsoleSpanExporter

# Set provider
trace.set_tracer_provider(TracerProvider())

tracer = trace.get_tracer(__name__)

# Add console exporter
span_processor = SimpleSpanProcessor(ConsoleSpanExporter())
trace.get_tracer_provider().add_span_processor(span_processor)

# Create span
with tracer.start_as_current_span("my-span"):
    print("Doing some work...")