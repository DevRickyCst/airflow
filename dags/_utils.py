from _hook import TelegramBotsHook



tl_hook = TelegramBotsHook()

def task_fail_alert_telegram(context):
    tl_hook.send_message(
        f"""
🔴 Task failed
    Task: {context["ti"].task_id}
    Dag: {context["ti"].dag_id}
    Execution Time: {context["execution_date"]}
    Log Url: {context["ti"].log_url}
        """
    )