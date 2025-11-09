(: Get average temperature across all reports in a DB :)
let $temps := //temperature
return
avg($temps/xs:decimal(.))