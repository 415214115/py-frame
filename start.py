from appRoute import creat_app
from appConfig.config import cfg


app = creat_app()
runCif = cfg.get_config('run')
if __name__ == "__main__":
    app.run(debug= runCif['run_debug'],host= runCif['run_host'],port= runCif['run_prot'])