import matplotlib.pyplot as plt

#SUPREME COURT SUPPORT
################################################################################

#supreme court decisions
plt.plot(sc_support.keys(),sc_support.values(),'ro',label='Supreme Court Supp. Vote Ratio')

plt.axhline(y=.5)

plt.legend()
plt.xlabel('Time (year)')
plt.ylabel('Support')
plt.title('SC Support for Gay Marriage')
plt.grid(True)

min_yr=min(list(sc_support.keys()))
plt.axis([min_yr-4, CURRENT_YEAR, 0.0, 1.1])

plt.savefig('./plots/sc_support.png', bbox_inches='tight')
#plt.show()
plt.gcf().clear()

#PUBLIC SUPPORT
################################################################################

#average public support for gay issues
plt.plot(all_po_avg.keys(),all_po_avg.values(),'mo',label='Public Support on LGBTQ Issues')

plt.axhline(y=.5)

plt.legend()
plt.xlabel('Time (year)')
plt.ylabel('Support')
plt.title('Public Support for Gay/Lesbian Issues')
plt.grid(True)

min_yr=min(list(sc_support.keys())+list(gay_temp_yr_avg.keys())+list(gay_mil_yr_avg.keys())+list(gay_adopt_yr_avg.keys()))
plt.axis([min_yr-4, CURRENT_YEAR, 0.0, 1.1])

plt.savefig('./plots/avg_po_support.png', bbox_inches='tight')
#plt.show()
plt.gcf().clear()

#SUPREME COURT v. PUBLIC OPINION
################################################################################

#public support for gay issues on average
plt.plot(all_po_avg.keys(),all_po_avg.values(),'bo',label='Public Support for Issue')

#supreme court decisions
plt.plot(sc_support.keys(),sc_support.values(),'ro',label='Supreme Court Supp. Vote Ratio')

plt.axhline(y=.5)

plt.legend()
plt.xlabel('Time (year)')
plt.ylabel('Support')
plt.title('SC v. PO for Gay/Lesbian Issues')
plt.grid(True)

min_yr=min(list(sc_support.keys())+list(all_po_avg.keys()))
plt.axis([min_yr-4, CURRENT_YEAR, 0.0, 1.1])

plt.savefig('./plots/avg_sc_v_po.png', bbox_inches='tight')
#plt.show()
plt.gcf().clear()

#EXAMPLE PLOTS
################################################################################
################################################################################
################################################################################

#PUBLIC OPINION SUPPORT for three LGBTQ issues
################################################################################

#public support for LGBTQ issues
plt.plot(gay_temp_yr_avg.keys(),gay_temp_yr_avg.values(),'g^',label='Gay/Lesbian Thermometer')
plt.plot(gay_mil_yr_avg.keys(),gay_mil_yr_avg.values(),'bs',label='Gays in the Military')
plt.plot(gay_adopt_yr_avg.keys(),gay_adopt_yr_avg.values(),'m.',label='Gays Adopting')

plt.axhline(y=.5)

plt.legend()
plt.xlabel('Time (year)')
plt.ylabel('Support')
plt.title('Public Support for LGBTQ Issues')
plt.grid(True)

min_yr=min(list(sc_support.keys())+list(gay_temp_yr_avg.keys())+list(gay_mil_yr_avg.keys())+list(gay_adopt_yr_avg.keys()))
plt.axis([min_yr-4, CURRENT_YEAR, 0.0, 1.1])

plt.savefig('./plots/po_support.png', bbox_inches='tight')
#plt.show()
plt.gcf().clear()



#SUPREME COURT v. PUBLIC OPINION for three LGBTQ questions
################################################################################

#public support for gay issues
plt.plot(gay_temp_yr_avg.keys(),gay_temp_yr_avg.values(),'g^',label='Gay/Lesbian Thermometer')
plt.plot(gay_mil_yr_avg.keys(),gay_mil_yr_avg.values(),'bs',label='Gays in the Military')
plt.plot(gay_adopt_yr_avg.keys(),gay_adopt_yr_avg.values(),'m.',label='Gays Adopting')

#supreme court decisions
plt.plot(sc_support.keys(),sc_support.values(),'ro',label='Supreme Court Supp. Vote Ratio')

plt.axhline(y=.5)

plt.legend()
plt.xlabel('Time (year)')
plt.ylabel('Support')
plt.title('SC v. PO for Gay/Lesbian Issues')
plt.grid(True)

min_yr=min(list(sc_support.keys())+list(gay_temp_yr_avg.keys())+list(gay_mil_yr_avg.keys())+list(gay_adopt_yr_avg.keys()))
plt.axis([min_yr-4, CURRENT_YEAR, 0.0, 1.1])

plt.savefig('./plots/sc_v_po.png', bbox_inches='tight')
#plt.show()
plt.gcf().clear()
