
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'common'))
# print(CommonPath)
from logfile import Logger
# from common
# from common.logfile import Logger


# from ..common.logfile import Logger 
# # import sys, os


# # print(os.getcwd())



filePath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'logs/haha.log')
log = Logger('haha', filePath)

log.log('hahahahahahahahaha')

print('__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(__file__,__name__,str(__package__)))