import logging
import structlog
import sys
log_format = "%(filename)s:%(lineno)s %(funcName)10s %(message)s"

logging.basicConfig(level='DEBUG',
		stream=sys.stdout,
		format=log_format)

chain = [
    structlog.stdlib.filter_by_level,
    structlog.stdlib.add_log_level,
    structlog.processors.StackInfoRenderer(),
    structlog.processors.format_exc_info,
    structlog.processors.JSONRenderer()
]

structlog.configure_once(
processors=chain,
context_class=dict,
logger_factory=structlog.stdlib.LoggerFactory(),
wrapper_class=structlog.stdlib.BoundLogger,
cache_logger_on_first_use=True,
)


# logger = logging.getLogger()
logger = structlog.get_logger()

if __name__=="__main__":
    logger.warning("strat")
    logger.warning("end")
    logger.error("done")
    logger.info("info")