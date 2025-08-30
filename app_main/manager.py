from .workers import news_scraper_api
import threading
class workers_handler:
    target_functions = []
    worker_name_running = []
    function_stat_handler = []
    thread_ = []
    def __init__(self,target_function, worker_name,arg=None,verbose:bool=True):
        self.target_function =target_function #storing the worker target function
        workers_handler.target_functions.append(self.target_function) #appending worker to target function to iterate the execution
        self.worker_name = worker_name 
        self.status = False # status of the worker function
        workers_handler.function_stat_handler.append(self) # storing child object in the function stat handler
        self.args_ = arg #arguments of the target function in case required for future changes
        self.verbose =  verbose
    @classmethod
    def run_workers(cls):
        for worker_instance in workers_handler.function_stat_handler:
            if worker_instance.status is True:
                continue
            worker_instance.status = True
            if worker_instance.args_ is not None:
                thread_process = threading.Thread(target=worker_instance.target_function, args=(worker_instance.args_,),name=worker_instance.worker_name )
                if worker_instance.verbose :
                    print(worker_instance.worker_name,"thread has been started.")
            else:
                thread_process = threading.Thread(target=worker_instance.target_function,name=worker_instance.worker_name )
                if worker_instance.verbose :
                    print(worker_instance.worker_name,"thread has been started.")
            thread_process.start()
            workers_handler.thread_.append(thread_process)


def run_manager():
    news_api = workers_handler(target_function=news_scraper_api._execute_api_, worker_name="news api scraper")
    workers_handler.run_workers()


        
