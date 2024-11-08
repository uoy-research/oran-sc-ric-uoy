#!/usr/bin/env python3

import time
import datetime
import argparse
import signal
from lib.xAppBase import xAppBase

class CellOffXapp(xAppBase):
    def __init__(self, config, http_server_port, rmr_port):
        super(CellOffXapp, self).__init__(config, http_server_port, rmr_port)
        pass

    # Mark the function as xApp start function using xAppBase.start_function decorator.
    # It is required to start the internal msg receive loop.
    @xAppBase.start_function
    def start(self, cell_id):
        while self.running:
            print("Sending the control command to turn off the cell")
            self.e2sm_rc.control_cell_power_state(cell_id,ack_request=1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Cell Off xApp')
    parser.add_argument("--config", type=str, default='', help="xApp config file path")
    parser.add_argument("--http_server_port", type=int, default=8090, help="HTTP server listen port")
    parser.add_argument("--rmr_port", type=int, default=4560, help="RMR port")
    parser.add_argument("--cell_id", type=str, default='gnbd_001_001_00019b_0', help="Cell ID to power off")

    args = parser.parse_args()
    config = args.config
    cell_id = args.cell_id

    # Create CellOffXapp instance
    cellOffXapp = CellOffXapp(config, args.http_server_port, args.rmr_port)

    # Connect exit signals
    signal.signal(signal.SIGQUIT, cellOffXapp.signal_handler)
    signal.signal(signal.SIGTERM, cellOffXapp.signal_handler)
    signal.signal(signal.SIGINT, cellOffXapp.signal_handler)

    # Start xApp with the target cell ID
    # cellOffXapp.start(cell_id)
    cellOffXapp.start("S9/N77/C1")
