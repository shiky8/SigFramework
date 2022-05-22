from setuptools import setup
setup(
    name='SigFramework',
    version='1.0.0',
    packages=['.','tracking','templates','simsi','mtsms','mtsms/test', 'UpdateLocation', 'static','static/images','static/templates', 'tracking/srism', 'tracking/srigprs', 'tracking/sri', 'tracking/psi',
              'tracking/ati','simsi/test', 'UpdateLocation/test',  'tracking/srism/test', 'tracking/srigprs/test', 'tracking/sri/test', 'tracking/psi/test',
              'tracking/ati/test'],
    url='https://github.com/shiky8',
    license='MIT',
    author='mohamed shahat',
    author_email='mohamedshahat028@gmail.com',
    description="SIG Framework it's an update for sigploit",
    install_requires=['PyQt5==5.15.6','flask==1.1.2'],
    entry_points={
        'console_scripts': [
            'SigFramework_cli=sig_framwork_cli:main_cli',
            'SigFramework_gui=sigfremwork_gui_main:main_gui',
            'SigFramework_web=sigframework_web:mainW'
        ]
    },
    package_data={
	'':['*.jpg','*.png','*.txt','*.json'],
	'static':['*.css','*.js','images/*.jpg','templates/*.json'],
	'simsi':['*.jar','test/*.jar'],
	'mtsms':['*.jar','test/*.jar'],
	'UpdateLocation':['*.jar','test/*.jar'],
	'tracking':['ati/*.jar','ati/test/*.jar','psi/*.jar','psi/test/*.jar','sri/*.jar','sri/test/*.jar','srigprs/*.jar','srigprs/test/*.jar','srism/*.jar','srism/test/*.jar'],

	'templates':['*.html','*.css','assets/js/*.js','assets/bootstrap/css/*.css','assets/img/*.png','assets/img/about/*.png','assets/img/portfolio/*.jpg','assets/img/team/*.jpg']
    }
  )
