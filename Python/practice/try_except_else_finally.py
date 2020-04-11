
import logging
logger =logging.getLogger()

if __name__=='__main__':
    try:
        i = 10 #/ 0
        # i = '10'
        # i +=1
    except ZeroDivisionError:
        i=None
    except Exception as e:
        logger.warning(e)
        i=0
    else:
        i=10
    finally:
        print("We doing good!")
        logger.warning(f'i={i}')
