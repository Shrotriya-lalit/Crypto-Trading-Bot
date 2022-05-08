import logging

from connectors.binance import BinanceClient
from connectors.bitmex import BitmexClient

from interface.root_component import Root


# Create and configure the logger object

logger = logging.getLogger()

logger.setLevel(logging.DEBUG)  # Overall minimum logging level

stream_handler = logging.StreamHandler()  # Configure the logging messages displayed in the Terminal
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)  # Minimum logging level for the StreamHandler

file_handler = logging.FileHandler('info.log')  # Configure the logging messages written to a file
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)  # Minimum logging level for the FileHandler

logger.addHandler(stream_handler)
logger.addHandler(file_handler)


if __name__ == '__main__':  # Execute the following code only when executing main.py (not when importing it)

    binance = BinanceClient("b5d72a9ec2e1106eb0135c70e93664260aa319c20354a908bbbcded25767e0c8",
                            "61439a1ed457ea466d1382f08c3ba2f56ea251bdb9e6990c0e406b176d85dce2",
                            testnet=True, futures=True)
    bitmex = BitmexClient("OPC2fOgpjfVggO-BT7fUIU-4", "xF9bbif2_v4FLjpEsZaqyWhj8HM2J-zDGxtQ32G4kyI5vfH8", testnet=True)

    root = Root(binance, bitmex)
    root.mainloop()
