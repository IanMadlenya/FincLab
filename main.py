"""
    Project : FincLab

    Author : Peter Lee

Three components of the system are dynamic - it means that you could replace these components in the 'config.ini" file with other classes to override the default:

    strategy : class, default to "MovingAverageCrossover"
        Strategy transforms the data feeds into investment signals, which will be received by the Portfolio class to determine the appropriate order size. Different strategies are available in the strategy folder.

    data_handler : class, default to "HistoricDataHandler"
        DataHandler transforms time series data (or live streams) into periodic "bars" to feed the event-driven system. The "HistoricDataHandler" is suitable for backtesting.

    execution_handler: class, default to "SimulatedExecutionHandler"
        Execution_hanlder executes the orders generated by the Portfolio class. The default "SimulatedExecutionHandler" assumes Interactive Brokers' brokerage fee and ignores market microstructure issues such as slippage, fill ratios etc.
"""

import datetime as dt
from portfolio import Portfolio
from engine import Engine
from config import config

# Dynamically import the remaining system components
exec("from data.{module} import {module} as DataHandler".format(module=config["components"]["data_handler"]))
exec("from execution.{module} import {module} as ExecutionHandler".format(module=config["components"]["execution_handler"]))
exec("from strategy.{module} import {module} as Strategy".format(module=config["components"]["strategy"]))

def finclab():
    # Program parameters
    initial_capital = 100000.0
    heartbeat = 0.0
    start_date = dt.datetime(2014, 1, 1, 0, 0, 0)
    symbol_list = ['AAPL']

    # Backtest
    engine = Engine(
        symbol_list=symbol_list,
        data_handler=DataHandler,
        execution_handler=ExecutionHandler,
        portfolio=Portfolio,
        strategy=Strategy,
        heartbeat=heartbeat,
        initial_capital=initial_capital,
        start_date=start_date
    )
    #engine.run()

if __name__ == "__main__":

    import logging
    import temp

    # create logger with 'spam_application'
    logger = logging.getLogger('WTF')
    logger.setLevel(logging.DEBUG)
    # create file handler which logs even debug messages
    fh = logging.FileHandler('finclab.log')
    fh.setLevel(logging.DEBUG)
    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    # add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)

    logger.info('creating an instance of temp.Auxiliary')
    a = temp.Auxiliary()
    logger.info('created an instance of temp.Auxiliary')
    logger.info('calling temp.Auxiliary.do_something')
    a.do_something()
    logger.info('finished temp.Auxiliary.do_something')
    logger.info('calling temp.some_function()')
    temp.some_function()
    logger.info('done with auxiliary_module.some_function()')

    finclab()
