import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

class CampusActivitySpider:
    def __init__(self, data_dir='data'):
        """初始化爬虫"""
        self.data_dir = data_dir
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
    
    def generate_sample_data(self, num_activities):
        """生成模拟数据"""
        np.random.seed(42)  # 设置随机种子保证结果可重复
        
        # 活动类型
        activity_types = ['学术讲座', '文艺演出', '体育比赛', '社团活动', '志愿活动', '招聘会', '竞赛活动']
        
        # 生成活动数据
        data = []
        today = datetime.now()
        
        for i in range(num_activities):
            activity_type = np.random.choice(activity_types)
            
            # 随机生成日期（过去30天到未来30天）
            days_offset = np.random.randint(-30, 31)
            date = today + timedelta(days=days_offset)
            
            # 生成其他数据
            activity = {
                'id': i + 1,
                'name': f'{activity_type}{i+1}',
                'type': activity_type,
                'date': date.strftime('%Y-%m-%d'),
                'location': np.random.choice(['体育馆', '学术报告厅', '操场', '学生活动中心', '线上']),
                'organizer': np.random.choice(['学生会', '团委', '教务处', '学生社团', '院系']),
                'heat': np.random.randint(1, 101),  # 热度评分 1-100
                'participants': np.random.randint(10, 1001)
            }
            data.append(activity)
        
        # 创建DataFrame
        df = pd.DataFrame(data)
        return df
    
    def save_data(self, df, format='all'):
        """保存数据到文件"""
        filename = f"campus_activities_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        if format == 'csv' or format == 'all':
            csv_path = os.path.join(self.data_dir, f"{filename}.csv")
            df.to_csv(csv_path, index=False, encoding='utf-8-sig')
            print(f"CSV文件已保存: {csv_path}")
        
        if format == 'excel' or format == 'all':
            excel_path = os.path.join(self.data_dir, f"{filename}.xlsx")
            df.to_excel(excel_path, index=False)
            print(f"Excel文件已保存: {excel_path}")
        
        if format == 'json' or format == 'all':
            json_path = os.path.join(self.data_dir, f"{filename}.json")
            df.to_json(json_path, orient='records', force_ascii=False)
            print(f"JSON文件已保存: {json_path}")
    
    def run(self, num_activities=20, use_real_data=False):
        """运行爬虫主程序"""
        print("=" * 60)
        print("校园活动数据爬虫 v2.0")
        print("负责人: 苏雪岚")
        print("任务: 获取校园活动数据")
        print("=" * 60)
        
        if use_real_data:
            print("真实数据爬取功能开发中...")
            print("暂时使用模拟数据")
        else:
            print("使用模拟数据进行演示...")
        
        # 生成数据
        df = self.generate_sample_data(num_activities)
        
        # 保存数据
        self.save_data(df, format='all')
        
        print("\n数据统计:")
        print(f"  活动总数: {len(df)}")
        print(f"  活动类型: {df['type'].nunique()} 种")
        print(f"  时间范围: {df['date'].min()} 到 {df['date'].max()}")
        print(f"  平均热度: {df['heat'].mean():.1f}")
        print(f"  总参与人数: {df['participants'].sum()}")
        
        print("=" * 60)
        print("爬虫任务完成!")
        print(f"数据文件保存在: {self.data_dir}/")
        print("=" * 60)
        
        return df


# 主程序入口
if __name__ == "__main__":
    # 创建爬虫实例
    spider = CampusActivitySpider()
    
    # 运行爬虫（使用模拟数据）
    df = spider.run(num_activities=25, use_real_data=False)
    
    # 显示数据概览
    print("\n数据概览（前5条）:")
    print(df.head().to_string())
    
    # 显示统计信息
    print("\n\n详细统计信息:")
    print("各类型活动数量:")
    print(df['type'].value_counts())
    
    print("\n活动热度分布:")
    print(f"最高热度: {df['heat'].max()}")
    print(f"最低热度: {df['heat'].min()}")
    print(f"中位数热度: {df['heat'].median()}")
