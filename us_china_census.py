import matplotlib.pyplot as plt

# Hardcoded data for each year, in chronological order
data = [
    # 2020
    {'year': '2020', 'months': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
     'exports': [7155.7, 6826.0, 7933.5, 8635.9, 9699.7, 9240.6, 9090.1, 10969.4, 11503.3, 14803.1, 14211.7, 14512.6],
     'imports': [32944.7, 22576.6, 19638.1, 30730.1, 36318.7, 37286.9, 40469.8, 40598.9, 41003.2, 44654.3, 44700.4, 41626.2],
     'balance': [-25788.9, -15750.6, -11704.6, -22094.3, -26619.1, -28046.2, -31379.8, -29629.6, -29499.9, -29851.2, -30488.7, -27113.6]},
    # 2021
    {'year': '2021', 'months': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
     'exports': [13011.2, 9265.1, 12812.0, 11931.4, 12407.4, 12142.6, 11757.3, 11245.2, 11019.6, 16651.5, 15883.8, 13312.4],
     'imports': [38835.3, 33816.8, 39934.0, 37371.1, 38486.5, 39779.3, 40290.9, 42897.8, 47350.9, 47873.5, 48234.8, 49375.3],
     'balance': [-25824.1, -24551.7, -27122.0, -25439.8, -26079.2, -27636.7, -28533.6, -31652.7, -36331.4, -31221.9, -32351.0, -36062.9]},
    # 2022
    {'year': '2022', 'months': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
     'exports': [11401.7, 11612.7, 13618.8, 11342.1, 12301.2, 11578.9, 12408.5, 12846.6, 11815.1, 15686.3, 15797.6, 13577.9],
     'imports': [47667.1, 42297.9, 47285.3, 41727.3, 43769.6, 48488.1, 46565.0, 50383.1, 49270.3, 44670.6, 36915.7, 37228.8],
     'balance': [-36265.3, -30685.1, -33666.5, -30385.2, -31468.4, -36909.2, -34156.6, -37536.6, -37455.1, -28984.3, -21118.0, -23650.9]},
    # 2023
    {'year': '2023', 'months': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
     'exports': [12979.9, 11782.2, 13869.1, 13066.1, 10705.2, 10078.2, 10799.2, 10783.0, 11780.2, 15805.3, 13936.3, 12050.7],
     'imports': [38166.1, 30569.8, 30791.6, 33071.4, 35881.0, 34312.8, 36108.1, 36828.5, 40247.9, 41548.5, 35537.4, 34183.6],
     'balance': [-25186.1, -18787.5, -16922.5, -20005.3, -25175.8, -24234.6, -25308.9, -26045.5, -28467.7, -25743.2, -21601.1, -22132.9]},
    # 2024
    {'year': '2024', 'months': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
     'exports': [12067.7, 12062.2, 12653.5, 11552.4, 11323.7, 11376.6, 10769.8, 11966.9, 11187.1, 13368.4, 12603.1, 12295.2],
     'imports': [35782.6, 31863.6, 29924.8, 31602.7, 34995.3, 34169.1, 40801.1, 39811.2, 43018.2, 41444.9, 37774.8, 37553.7],
     'balance': [-23714.9, -19801.4, -17271.2, -20050.3, -23671.5, -22792.5, -30031.3, -27844.3, -31831.1, -28076.5, -25171.8, -25258.5]},
    # 2025 (Jan–Apr)
    {'year': '2025', 'months': ['Jan', 'Feb', 'Mar', 'Apr'],
     'exports': [9901.3, 10461.6, 11458.2, 8193.1],
     'imports': [41639.2, 31635.4, 29383.7, 25378.1],
     'balance': [-31737.8, -21173.8, -17925.5, -17185.0]}
]

# Concatenate all months, exports, imports, balance in chronological order
all_months = []
all_exports = []
all_imports = []
all_balance = []

for year_data in data:
    for i, month in enumerate(year_data['months']):
        all_months.append(f"{month} {year_data['year']}")
        all_exports.append(year_data['exports'][i])
        all_imports.append(year_data['imports'][i])
        all_balance.append(year_data['balance'][i])

# Plotting
plt.figure(figsize=(16, 8))
plt.plot(all_months, all_exports, marker='o', markersize=4, label='Exports')
plt.plot(all_months, all_imports, marker='s', markersize=4, label='Imports')
plt.plot(all_months, all_balance, marker='^', markersize=4, linestyle='--', label='Balance')

plt.axhline(0, color='black', linewidth=0.5)
plt.xlabel('Month and Year')
plt.ylabel('Millions of USD')
plt.title('U.S. Trade in Goods with China (Jan 2020 – Apr 2025)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
