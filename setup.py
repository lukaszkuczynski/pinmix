from setuptools import setup

setup(
        name='pinmix',
        version='0.1',
        packages=['pinmix'],
        install_requires=[
		'jieba',
		'xpinyin==0.5.5',
		'odfpy'
	],
        entry_points={
            'console_scripts':['pinmix=pinmix.cmdline:main']
        }
)

