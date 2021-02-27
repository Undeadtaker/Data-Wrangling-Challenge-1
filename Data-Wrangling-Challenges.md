## Challenge 1

Your task: write a script to get a nice CSV file of natural gas prices.

Please publish your results in a git repo or a gist. Please include both script **and** your resulting data -- so the CSV files should be stored in the repo too!

More detail:

* Prices should be Henry Hub gas prices. Use EIA data here: http://www.eia.gov/dnav/ng/hist/rngwhhdm.htm
  * *Hint: you can get the data from any data source on the page ...*
* Main data wanted is **daily** prices.
  * Bonus points for doing other granularities (e.g. month) - do them in separate CSV files with sensible naming
* Resulting CSV should have **two** columns: Date and Price. You may need to normalize the data to get this and/or work out dates. For months the Date should be the first date of the month.
* We want a **script** for this and we want this script to be in **python** (we'd allow node or bash or go script at a push but prefer python)
  * Why a script? Ans: We'll want to run this again and again as they release new data. You could copy and paste data into Excel/Google Docs by hand, and then export the CSV. But that would be tedious, time consuming and error prone to do month after month
  * Please use simple python libraries wherever possible rather than use a framework

Bonus items (optional - extra kudos if you do either of these!):

* Make your repository into a Tabular Data Package - here's a [guide](http://datahub.io/docs/data-packages/publish-tabular)
* Do a line graph visualization of the data in HTML + Javascript using e.g. vega or direct in D3
  * Deploy your repo somewhere so this visualization is visitable online e.g. via github or gitlab pages
