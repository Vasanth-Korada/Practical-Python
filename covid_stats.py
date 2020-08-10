from covid import Covid

covid  = Covid()

print("\nALL DATA:"+str(covid.get_data()))
print("\nITALY CASES:"+str(covid.get_status_by_country_name("italy")))
print("\nACTIVE CASES:"+str(covid.get_total_active_cases()))
print("\nCONFIRMED CASES:"+str(covid.get_total_confirmed_cases()))
print("\nRECOVERED CASES:"+str(covid.get_total_recovered()))
print("\nTOTAL DEATHS:"+str(covid.get_total_deaths()))

