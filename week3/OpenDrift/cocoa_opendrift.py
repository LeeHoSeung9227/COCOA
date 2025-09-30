from datetime import datetime, timedelta
from opendrift.readers import reader_netCDF_CF_generic
from opendrift.models.oceandrift import OceanDrift
import matplotlib.pyplot as plt
from datetime import timedelta

# 모델 초기화
o = OceanDrift(loglevel=20)

# 리더 추가
reader_wind = reader_netCDF_CF_generic.Reader('본인의 바람 파일을 경로를 작성하세요')
reader_current = reader_netCDF_CF_generic.Reader('본인의 해류 파일의 경로를 작성하세요')
o.add_reader([reader_wind, reader_current])

# ⚠️ Config 설정
o.set_config('drift:vertical_mixing', True)
o.set_config('vertical_mixing:timestep', 60)
o.set_config('general:coastline_action', 'previous')
o.set_config('drift:horizontal_diffusivity', 0.25)  #  확산 추가

# 입자 시딩
start_time = reader_wind.start_time
end_time = start_time + timedelta(days=30)  #  30일 시뮬레이션

# 입자 시딩 (시작 시간은 여기서 설정됨)
o.seed_elements(lon=128.5, lat=34.1, number=50, radius=5, time=start_time)


# 시뮬레이션 실행
o.run(
    end_time=end_time,  #  종료 시간만 설정!
    time_step=900,
    time_step_output=3600,
    outfile='point_4_30days.nc',
    export_variables=['z', 'age_seconds']
)

# 결과 시각화
o.plot(fast=False)


