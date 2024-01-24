"""
Logging Config, imported at the end of common.py
"""
import json_log_formatter
import json


class CustomJsonFormatter(json_log_formatter.JSONFormatter):
    def json_record(self, message, extra, record):
        _ = extra.pop("request", None)
        extra.update(
            {
                "level": record.levelname,
                "pathname": record.pathname,
                "caller": record.filename + "::" + record.funcName,
                "logger_name": record.name,
                "module": record.module,
                "funcName": record.funcName,
                "filename": record.filename,
                "lineno": record.lineno,
                "thread": record.threadName,
                "pid": record.process,
                "application_name": "rentdoor",
            }
        )
        return super().json_record(message, extra, record)


class RequestResponseFormatter(json_log_formatter.JSONFormatter):
    def json_record(self, message, extra, record):
        _ = extra.pop("request", None)
        record_dict = record.__dict__.items()
        record_msg_list = list(record_dict)[1][1]
        extra.update(
            {
                "execution_time": record_msg_list["execution_time"],
                "ip_address": record_msg_list["ip_address"],
                "method": record_msg_list["request"]["method"],
                "full_path": record_msg_list["request"]["full_path"],
                "query_params": record_msg_list["request"]["query_params"],
                "req_params": record_msg_list["request"]["data"],
                "status_code": record_msg_list["response"]["status_code"],
                "data": json.loads(record_msg_list["response"]["data"]),
                "level": record.levelname,
                "caller": record.filename + "::" + record.funcName,
                "logger_name": record.name,
                "module": record.module,
                "funcName": record.funcName,
                "filename": record.filename,
                "lineno": record.lineno,
                "thread": record.threadName,
                "pid": record.process,
                "application_name": "rentdoor",
            }
        )
        return super().json_record(message, extra, record)
