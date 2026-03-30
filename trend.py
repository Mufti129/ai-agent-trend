from pytrends.request import TrendReq

def get_trend():
    pytrends = TrendReq()
    pytrends.build_payload(kw_list=["fashion wanita", "dress lebaran"])

    data = pytrends.interest_over_time()
    return data.tail().to_string()
