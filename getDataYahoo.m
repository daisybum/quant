% add system path
addpath('functions')

% Download data from Yahoo
initDate = '1-Sep-2020';
symbol = 'AAPL';
aaplusd_yahoo_raw = getMarketDataViaYahoo(symbol, initDate);
aaplusd_yahoo = timeseries([aaplusd_yahoo_raw.Close, ...
    aaplusd_yahoo_raw.High, aaplusd_yahoo_raw.Low], ...
    datestr(aaplusd_yahoo_raw(:, 1).Date));
aaplusd_yahoo.DataInfo.Units = 'USE';
aaplusd_yahoo.Name = symbol;
aaplusd_yahoo.TimeInfo.Format = "dd-mm-yyyy";

figure,
plot(aaplusd_yahoo);
legend({'Close', 'High', 'Low'}, 'Location', 'northwest');
disp(aaplusd_yahoo_raw.Close)
