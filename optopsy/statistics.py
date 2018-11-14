#     Optopsy - Python Backtesting library for options trading strategies
#     Copyright (C) 2018  Michael Chu

#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.

#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.

#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.

def calc_entry_px(data, mode='midpoint'):
    if mode == 'midpoint':
        return data.assign(
            entry_opt_price=data[['bid_entry', 'ask_entry']].mean(axis=1))
    elif mode == 'market':
        return data.assign(entry_opt_price=data['ask_entry'])


def calc_exit_px(data, mode='midpoint'):
    if mode == 'midpoint':
        return data.assign(
            exit_opt_price=data[['bid_exit', 'ask_exit']].mean(axis=1))
    elif mode == 'market':
        return data.assign(exit_opt_price=data['ask_exit'])


def calc_pnl(data):
    # calculate the p/l for the trades
    data['entry_price'] = data['entry_opt_price'] * \
        data['ratio'] * data['contracts']
    data['exit_price'] = data['exit_opt_price'] * \
        data['ratio'] * data['contracts']
    data['profit'] = data['exit_price'] - data['entry_price']
    return data


def calc_total_profit(data):
    return data['profit'].sum().round(2)