import time
import logging
from typing import Dict, Any, Optional
from contextlib import asyncontextmanager
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

class MetricsCollector:
    """A simple metrics collector for tracking API usage and performance."""

    def __init__(self):
        self.metrics: Dict[str, list] = {
            "query_latency": [],
            "tool_latency": [],
            "cache_hits": [],
            "cache_misses": [],
            "errors": []
        }
    
    def record_latency(self, operation: str, latency_ms: float):
        """Record the latency of a specific operation."""
        self.metrics["tool_latency"].append({
            "operation": operation,
            "latency_ms": latency_ms,
            "timestamp": datetime.now()
        })
        logger.info(f"Recorded latency for {operation}: {latency_ms:.2f} ms")
    
    def record_cache_hit(self, query: str):
        """Record cache hit."""
        self.metrics["cache_hits"].append({
            "query": query,
            "timestamp": datetime.now()
        })
        logger.info(f"Cache hit for query: {query[:50]}...")
    
    def record_cache_miss(self, query: str):
        """Record cache miss."""
        self.metrics["cache_misses"].append({
            "query": query,
            "timestamp": datetime.now()
        })
        logger.info(f"Cache miss for query: {query[:50]}...")
    
    def record_error(self, operation: str, error: Exception):
        """Record error."""
        self.metrics["errors"].append({
            "operation": operation,
            "error": str(error),
            "timestamp": datetime.now()
        })
        logger.error(f"Error in {operation}: {error}")

    def get_summary(self) -> Dict[str, Any]:
        """Get a summary of the collected metrics."""
        total_cache = len(self.metrics["cache_hits"]) + len(self.metrics["cache_misses"])
        cache_hit_rate = (len(self.metrics["cache_hits"]) / total_cache if total_cache > 0 else 0)
        avg_latency = (sum(m["latency_ms"] for m in self.metrics["tool_latency"]) / max(1, len(self.metrics["tool_latency"])))
        
        return {
            "total_queries": len(self.metrics["tool_latency"]),
            "average_latency_ms": avg_latency,
            "cache_hit_rate": cache_hit_rate,
            "total_errors": len(self.metrics["errors"])
        }

@asyncontextmanager
async def track_latency(metrics_collector: MetricsCollector, operation: str):
    """Context manager to track latency of an operation."""
    start_time = time.time()
    try:
        yield
    except Exception as e:
        metrics_collector.record_error(operation, e)
        raise
    finally:
        end_time = time.time()
        latency_ms = (end_time - start_time) * 1000
        metrics_collector.record_latency(operation, latency_ms)

metrics = MetricsCollector()