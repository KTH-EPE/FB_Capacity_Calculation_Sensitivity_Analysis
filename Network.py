import pypowsybl as pp
import pandas as pd
import numpy as np

def setup_N32_network(N32):
    # ============================================================
    # 1. GEO-COORDINATES
    # ============================================================
    N32.create_extensions('substationPosition', pd.DataFrame.from_records(index='id', data=[
        {'id': 'SUB-1',  'latitude': 67.8,       'longitude': 19.827881},
        {'id': 'SUB-3',  'latitude': 58.57374,   'longitude': 11.996662},
        {'id': 'SUB-4',  'latitude': 57.035525,  'longitude': 16.502903},
        {'id': 'SUB-5',  'latitude': 60.235525,  'longitude': 14.002903},
        {'id': 'SUB-6',  'latitude': 59.656389,  'longitude': 17.182421},
        {'id': 'SUB-7',  'latitude': 65.386818,  'longitude': 27.312569},
        {'id': 'SUB-8',  'latitude': 58.535525,  'longitude': 16.502903},
        {'id': 'SUB-9',  'latitude': 67.387671,  'longitude': 26.607238},
        {'id': 'SUB-10', 'latitude': 60.656389,  'longitude': 16.282421},
        {'id': 'SUB-11', 'latitude': 60.056389,  'longitude': 18.082421},
        {'id': 'SUB-12', 'latitude': 64.956333,  'longitude': 19.487919},
        {'id': 'SUB-13', 'latitude': 63.574554,  'longitude': 11.420925},
        {'id': 'SUB-14', 'latitude': 59.835525,  'longitude': 14.402903},
        {'id': 'SUB-16', 'latitude': 58.635525,  'longitude': 15.202903},
        {'id': 'SUB-17', 'latitude': 67.05019,   'longitude': 16.544969},
        {'id': 'SUB-18', 'latitude': 57.035525,  'longitude': 13.494514},
        {'id': 'SUB-19', 'latitude': 63.574554,  'longitude': 13.898688},
        {'id': 'SUB-21', 'latitude': 64.956333,  'longitude': 12.203632},
        {'id': 'SUB-22', 'latitude': 64.956333,  'longitude': 15.049038},
        {'id': 'SUB-24', 'latitude': 66.056051,  'longitude': 15.338445},
        {'id': 'SUB-26', 'latitude': 55.835525,  'longitude': 13.094514},
        {'id': 'SUB-27', 'latitude': 58.035525,  'longitude': 14.002903},
        {'id': 'SUB-29', 'latitude': 63.574554,  'longitude': 17.282421},
        {'id': 'SUB-30', 'latitude': 60.056389,  'longitude': 16.282421},
        {'id': 'SUB-31', 'latitude': 68.019844,  'longitude': 17.475847},
        {'id': 'SUB-32', 'latitude': 59.235525,  'longitude': 14.902903},
    ]))
    print("✓ Geo-coordinates applied")

    # ============================================================
    # 2a. SUBSTATION NAMES
    # ============================================================
    sub_names = {
        'SUB-1':  'AGGAN CT11',       'SUB-3':  'ATOMSBERG FT61',
        'SUB-4':  'BLOCKET FT51',     'SUB-5':  'DALBO FT41',
        'SUB-6':  'ERIKSHAMN FT47',   'SUB-7':  'HÄLLAN CT72',
        'SUB-8':  'HÄSTSJÖ RT132',    'SUB-9':  'JAURAS CT71',
        'SUB-10': 'KÄRNAN FT44',      'SUB-11': 'MITTLANDA FT45',
        'SUB-12': 'NJAGGO CT21',      'SUB-13': 'NORRSELE AT241',
        'SUB-14': 'NORRÅS FT42',      'SUB-16': 'NYSTAD RT133',
        'SUB-17': 'OLMÅFALLET AT121', 'SUB-18': 'RUTHUVUD FT62',
        'SUB-19': 'STENFORSEN CT31',  'SUB-21': 'STORFORS AT131',
        'SUB-22': 'STORTRÄSK CT22',   'SUB-24': 'STUPET CT12',
        'SUB-26': 'SYDBÄCK FT63',     'SUB-27': 'SYDKÖPING FT50',
        'SUB-29': 'TORNÅ CT32',       'SUB-30': 'UPPMARK FT43',
        'SUB-31': 'VATTENDRAGET AT111', 'SUB-32': 'YTTERFORSEN RT131',
    }

    N32.update_substations(pd.DataFrame(
        index=pd.Series(list(sub_names.keys()), name='id'),
        data={'name': list(sub_names.values())}
    ))
    print("✓ Substation names applied")

    # ============================================================
    # 2b. VOLTAGE LEVEL NAMES
    # ============================================================
    vl_names = {
        'VL-1':  'AGGAN CT11_135.0kV',          'VL-2':  'AGGAN CT11_400.0kV',
        'VL-3':  'ATOMSBERG FT61_400.0kV',       'VL-4':  'BLOCKET FT51_400.0kV',
        'VL-5':  'DALBO FT41_400.0kV',           'VL-6':  'ERIKSHAMN FT47_400.0kV',
        'VL-7':  'HÄLLAN CT72_400.0kV',          'VL-8':  'HÄSTSJÖ RT132_135.0kV',
        'VL-9':  'JAURAS CT71_400.0kV',          'VL-10': 'KÄRNAN FT44_400.0kV',
        'VL-11': 'MITTLANDA FT45_400.0kV',       'VL-12': 'NJAGGO CT21_400.0kV',
        'VL-13': 'NORRSELE AT241_220.0kV',       'VL-14': 'NORRÅS FT42_135.0kV',
        'VL-15': 'NORRÅS FT42_400.0kV',          'VL-16': 'NYSTAD RT133_135.0kV',
        'VL-17': 'OLMÅFALLET AT121_135.0kV',     'VL-18': 'RUTHUVUD FT62_400.0kV',
        'VL-19': 'STENFORSEN CT31_220.0kV',      'VL-20': 'STENFORSEN CT31_400.0kV',
        'VL-21': 'STORFORS AT131_135.0kV',       'VL-22': 'STORTRÄSK CT22_135.0kV',
        'VL-23': 'STORTRÄSK CT22_400.0kV',       'VL-24': 'STUPET CT12_135.0kV',
        'VL-25': 'STUPET CT12_400.0kV',           'VL-26': 'SYDBÄCK FT63_400.0kV',
        'VL-27': 'SYDKÖPING FT50_135.0kV',       'VL-28': 'SYDKÖPING FT50_400.0kV',
        'VL-29': 'TORNÅ CT32_400.0kV',           'VL-30': 'UPPMARK FT43_400.0kV',
        'VL-31': 'VATTENDRAGET AT111_135.0kV',   'VL-32': 'YTTERFORSEN RT131_135.0kV',
    }

    N32.update_voltage_levels(pd.DataFrame(
        index=pd.Series(list(vl_names.keys()), name='id'),
        data={'name': list(vl_names.values())}
    ))
    print("✓ Voltage level names applied")

    # ============================================================
    # 2c. LINE NAMES (generated from substations)
    # ============================================================
    vl = N32.get_voltage_levels()
    subs = N32.get_substations()
    lines = N32.get_lines()

    vl_info = vl.merge(
        subs[['name']].rename(columns={'name': 'sub_name'}),
        left_on='substation_id', right_index=True
    )

    base_names = {}
    parallel_count = {}
    for line_id, row in lines.iterrows():
        sub1 = vl_info.loc[row['voltage_level1_id'], 'sub_name']
        sub2 = vl_info.loc[row['voltage_level2_id'], 'sub_name']
        voltage = vl_info.loc[row['voltage_level1_id'], 'nominal_v']
        base = f"{sub1} - {sub2} {voltage:.0f}kV"

        core_id = line_id.split('#')[0]
        if core_id not in parallel_count:
            parallel_count[core_id] = []
        parallel_count[core_id].append(line_id)
        base_names[line_id] = base

    line_names = {}
    for core_id, line_ids in parallel_count.items():
        if len(line_ids) == 1:
            line_names[line_ids[0]] = base_names[line_ids[0]]
        else:
            for i, lid in enumerate(line_ids):
                line_names[lid] = base_names[lid] + f" #{i+1}"

    N32.update_lines(pd.DataFrame(
        index=pd.Series(list(line_names.keys()), name='id'),
        data={'name': list(line_names.values())}
    ))
    print(f"✓ Line names applied ({len(line_names)} lines)")

    # ============================================================
    # 2d. TRANSFORMER NAMES
    # ============================================================
    trafo_data = {
        'TWT-2-1':     {'name': 'AGGAN CT11 400/135kV',        'i_kA': 1.53},
        'TWT-25-24':   {'name': 'STUPET CT12 400/135kV',       'i_kA': 1.53},
        'TWT-23-22':   {'name': 'STORTRÄSK CT22 400/135kV',    'i_kA': 1.53},
        'TWT-20-19':   {'name': 'STENFORSEN CT31 400/220kV',   'i_kA': 1.53},
        'TWT-28-27':   {'name': 'SYDKÖPING FT50 400/135kV #1', 'i_kA': 1.58},
        'TWT-28-27#0': {'name': 'SYDKÖPING FT50 400/135kV #2', 'i_kA': 1.58},
        'TWT-15-14':   {'name': 'NORRÅS FT42 400/135kV #1',    'i_kA': 0.94},
        'TWT-15-14#0': {'name': 'NORRÅS FT42 400/135kV #2',    'i_kA': 0.94},
    }

    N32.update_2_windings_transformers(pd.DataFrame(
        index=pd.Series(list(trafo_data.keys()), name='id'),
        data={'name': [d['name'] for d in trafo_data.values()]}
    ))
    print(f"✓ Transformer names applied ({len(trafo_data)} trafos)")

    # ============================================================
    # 3. LINE OPERATIONAL LIMITS
    # ============================================================
    thermal_limits_kA = {
        'LINE-2-9': 1.02, 'LINE-2-12': 1.53, 'LINE-2-23': 1.53,
        'LINE-2-25': 3.60, 'LINE-25-9': 1.02, 'LINE-9-7': 3.00,
        'LINE-9-7#0': 3.00, 'LINE-25-23': 1.53, 'LINE-23-20': 1.53,
        'LINE-23-20#0': 1.53, 'LINE-12-29': 1.53, 'LINE-12-10': 1.53,
        'LINE-20-29': 3.60, 'LINE-20-5': 1.53, 'LINE-20-5#0': 1.53,
        'LINE-29-15': 1.53, 'LINE-29-10': 1.53,
        'LINE-10-30': 1.53, 'LINE-5-15': 1.53, 'LINE-30-15': 1.53,
        'LINE-30-11': 1.53, 'LINE-11-6': 2.96, 'LINE-5-3': 1.02,
        'LINE-15-28': 2.96, 'LINE-15-28#0': 2.96, 'LINE-30-6': 1.53,
        'LINE-3-18': 2.97, 'LINE-28-18': 1.02, 'LINE-18-26': 1.53,
        'LINE-18-26#0': 1.53, 'LINE-28-4': 1.53, 'LINE-28-4#0': 1.53,
        'LINE-10-15': 1.53,
        'LINE-1-31': 2.10, 'LINE-1-31#0': 2.10, 'LINE-31-17': 1.07,
        'LINE-31-17#0': 1.07, 'LINE-24-17': 1.53, 'LINE-24-17#0': 1.53,
        'LINE-21-22': 1.53, 'LINE-21-22#0': 1.53, 'LINE-19-13': 1.53,
        'LINE-19-13#0': 1.53,
        'LINE-8-14': 1.53, 'LINE-8-14#0': 1.53, 'LINE-32-14': 1.53,
        'LINE-32-14#0': 1.53, 'LINE-16-32': 2.97, 'LINE-16-32#0': 2.97,
        'LINE-8-27': 1.53, 'LINE-16-27': 1.53, 'LINE-16-27#0': 1.53,
    }

    vl = N32.get_voltage_levels()
    lines = N32.get_lines()

    records = []
    Fmax = {}
    for line_id, i_max_kA in thermal_limits_kA.items():
        vl_id = lines.loc[line_id, 'voltage_level1_id']
        v_nom = vl.loc[vl_id, 'nominal_v']
        s_max = round(np.sqrt(3) * v_nom * i_max_kA, 1)
        Fmax[line_id] = s_max

        for side in ['ONE', 'TWO']:
            for limit_type in ['APPARENT_POWER', 'ACTIVE_POWER']:
                records.append({
                    'element_id': line_id,
                    'element_type': 'LINE',
                    'side': side,
                    'type': limit_type,
                    'name': 'permanent_limit',
                    'value': s_max,
                    'acceptable_duration': -1,
                })

    N32.create_operational_limits(
        pd.DataFrame.from_records(records).set_index('element_id')
    )
    print(f"✓ Line limits applied ({len(thermal_limits_kA)} lines)")

    # ============================================================
    # 4. TRANSFORMER OPERATIONAL LIMITS
    # ============================================================
    V_HV = 400
    records = []
    for twt_id, data in trafo_data.items():
        s_mva = round(np.sqrt(3) * V_HV * data['i_kA'], 1)
        for side in ['ONE', 'TWO']:
            records.append({
                'element_id': twt_id,
                'element_type': 'TWO_WINDINGS_TRANSFORMER',
                'side': side,
                'type': 'APPARENT_POWER',
                'name': 'permanent_limit',
                'value': s_mva,
                'acceptable_duration': -1,
            })

    N32.create_operational_limits(
        pd.DataFrame.from_records(records).set_index('element_id')
    )
    print(f"✓ Transformer limits applied ({len(trafo_data)} trafos)")

    # ============================================================
    # Summary
    # ============================================================
    print(f"\n{'=' * 50}")
    print("SETUP COMPLETE")
    print(f"{'=' * 50}")
    print(f"  Substations:  {len(sub_names)}")
    print(f"  Voltage levels: {len(vl_names)}")
    print(f"  Lines:        {len(line_names)} (with limits)")
    print(f"  Transformers: {len(trafo_data)} (with limits)")

    return Fmax, thermal_limits_kA, trafo_data
