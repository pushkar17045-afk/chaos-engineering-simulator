## Latency Injection Experiment

**Objective**
Study system behavior when Service B experiences high latency.

**Setup**
Injected 3s delay into Service B.

**Observations**
- Service A returned degraded responses
- Timeout occurred after 2s
- No cascading crash observed

**Conclusion**
Timeouts prevent full system failure but cause partial degradation.
