using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using System.Windows.Forms;
using System.Windows.Forms.DataVisualization.Charting;

namespace WinFormsApp2
{
    public partial class AnnualReportForm : Form
    {
        private List<Transaction> transactions;
        private Chart chart;
        private ComboBox cmbChartType;
        private ComboBox cmbYear;
        private Panel statsPanel;

        public AnnualReportForm(List<Transaction> transactions)
        {
            this.transactions = transactions;
            InitializeComponent();
            SetupUI();
            LoadYears();
        }

        private void InitializeComponent()
        {
            SuspendLayout();
            // 
            // AnnualReportForm
            // 
            ClientSize = new Size(978, 644);
            Name = "AnnualReportForm";
            StartPosition = FormStartPosition.CenterParent;
            Text = "年度財報";
            Load += AnnualReportForm_Load;
            ResumeLayout(false);
        }

        private void SetupUI()
        {
            // Top panel for controls
            Panel topPanel = new Panel
            {
                Dock = DockStyle.Top,
                Height = 60,
                Padding = new Padding(10)
            };

            Label lblYear = new Label
            {
                Text = "年度:",
                Location = new Point(10, 20),
                AutoSize = true
            };

            cmbYear = new ComboBox
            {
                Location = new Point(60, 17),
                Width = 100,
                DropDownStyle = ComboBoxStyle.DropDownList
            };
            cmbYear.SelectedIndexChanged += (s, e) => UpdateChart();

            Label lblChartType = new Label
            {
                Text = "圖表類型:",
                Location = new Point(180, 20),
                AutoSize = true
            };

            cmbChartType = new ComboBox
            {
                Location = new Point(260, 17),
                Width = 120,
                DropDownStyle = ComboBoxStyle.DropDownList
            };
            cmbChartType.Items.AddRange(new object[] { "圓餅圖", "折線圖" });
            cmbChartType.SelectedIndex = 0;
            cmbChartType.SelectedIndexChanged += (s, e) => UpdateChart();

            topPanel.Controls.AddRange(new Control[] { lblYear, cmbYear, lblChartType, cmbChartType });

            // Stats panel
            statsPanel = new Panel
            {
                Dock = DockStyle.Top,
                Height = 100,
                Padding = new Padding(10)
            };

            // Chart
            chart = new Chart
            {
                Dock = DockStyle.Fill
            };
            chart.ChartAreas.Add(new ChartArea("MainArea"));
            chart.Legends.Add(new Legend("MainLegend"));

            this.Controls.Add(chart);
            this.Controls.Add(statsPanel);
            this.Controls.Add(topPanel);
        }

        private void LoadYears()
        {
            var years = transactions.Select(t => t.Date.Year).Distinct().OrderByDescending(y => y).ToList();
            if (!years.Any())
            {
                years.Add(DateTime.Now.Year);
            }

            cmbYear.Items.Clear();
            foreach (var year in years)
            {
                cmbYear.Items.Add(year);
            }

            if (cmbYear.Items.Count > 0)
            {
                cmbYear.SelectedIndex = 0;
            }
        }

        private void UpdateChart()
        {
            if (cmbYear.SelectedItem == null) return;

            int selectedYear = (int)cmbYear.SelectedItem;
            var yearTransactions = transactions.Where(t => t.Date.Year == selectedYear).ToList();

            chart.Series.Clear();
            chart.Titles.Clear();
            chart.Titles.Add($"{selectedYear}年度財務報表");

            UpdateStats(yearTransactions);

            if (cmbChartType.SelectedIndex == 0)
            {
                ShowPieChart(yearTransactions);
            }
            else
            {
                ShowLineChart(yearTransactions, selectedYear);
            }
        }

        private void UpdateStats(List<Transaction> yearTransactions)
        {
            statsPanel.Controls.Clear();

            decimal totalIncome = yearTransactions.Where(t => t.Type == TransactionType.收入).Sum(t => t.Amount);
            decimal totalExpense = yearTransactions.Where(t => t.Type == TransactionType.支出).Sum(t => t.Amount);
            decimal netProfit = totalIncome - totalExpense;

            Label lblStats = new Label
            {
                AutoSize = true,
                Location = new Point(10, 10),
                Font = new Font("Microsoft JhengHei", 12, FontStyle.Bold)
            };
            lblStats.Text = $"總收入: {totalIncome:C0}    總支出: {totalExpense:C0}    淨利潤: {netProfit:C0}";
            if (netProfit >= 0)
            {
                lblStats.ForeColor = Color.Green;
            }
            else
            {
                lblStats.ForeColor = Color.Red;
            }

            // Monthly breakdown
            Label lblMonthly = new Label
            {
                AutoSize = true,
                Location = new Point(10, 40),
                Font = new Font("Microsoft JhengHei", 10)
            };

            var monthlyData = yearTransactions
                .GroupBy(t => t.Date.Month)
                .OrderBy(g => g.Key)
                .Select(g => new
                {
                    Month = g.Key,
                    Income = g.Where(t => t.Type == TransactionType.收入).Sum(t => t.Amount),
                    Expense = g.Where(t => t.Type == TransactionType.支出).Sum(t => t.Amount)
                })
                .ToList();

            string monthlyInfo = "月度損益: ";
            foreach (var m in monthlyData)
            {
                decimal profit = m.Income - m.Expense;
                monthlyInfo += $"{m.Month}月: {profit:C0}  ";
            }
            lblMonthly.Text = monthlyInfo;

            statsPanel.Controls.AddRange(new Control[] { lblStats, lblMonthly });
        }

        private void ShowPieChart(List<Transaction> yearTransactions)
        {
            Series series = new Series
            {
                Name = "財務分析",
                ChartType = SeriesChartType.Pie
            };

            decimal totalIncome = yearTransactions.Where(t => t.Type == TransactionType.收入).Sum(t => t.Amount);
            decimal totalExpense = yearTransactions.Where(t => t.Type == TransactionType.支出).Sum(t => t.Amount);

            if (totalIncome > 0)
            {
                var point = series.Points.Add((double)totalIncome);
                point.Label = $"收入\n{totalIncome:C0}";
                point.Color = Color.LightGreen;
                point.LegendText = "收入";
            }

            if (totalExpense > 0)
            {
                var point = series.Points.Add((double)totalExpense);
                point.Label = $"支出\n{totalExpense:C0}";
                point.Color = Color.LightCoral;
                point.LegendText = "支出";
            }

            series["PieLabelStyle"] = "Outside";
            series["PieLineColor"] = "Black";

            chart.Series.Add(series);
            chart.ChartAreas[0].Area3DStyle.Enable3D = true;
        }

        private void ShowLineChart(List<Transaction> yearTransactions, int year)
        {
            // 設定為平面樣式（禁用 3D）
            chart.ChartAreas[0].Area3DStyle.Enable3D = false;
            
            // 設定圖表背景和格線
            chart.ChartAreas[0].BackColor = Color.White;
            chart.ChartAreas[0].AxisX.MajorGrid.LineColor = Color.LightGray;
            chart.ChartAreas[0].AxisY.MajorGrid.LineColor = Color.LightGray;
            chart.ChartAreas[0].AxisX.LineColor = Color.Gray;
            chart.ChartAreas[0].AxisY.LineColor = Color.Gray;

            Series incomeSeries = new Series
            {
                Name = "收入",
                ChartType = SeriesChartType.Line,
                BorderWidth = 3,
                Color = Color.Green,
                MarkerStyle = MarkerStyle.Circle,
                MarkerSize = 8,
                ShadowOffset = 0  // 移除陰影效果
            };

            Series expenseSeries = new Series
            {
                Name = "支出",
                ChartType = SeriesChartType.Line,
                BorderWidth = 3,
                Color = Color.Red,
                MarkerStyle = MarkerStyle.Circle,
                MarkerSize = 8,
                ShadowOffset = 0  // 移除陰影效果
            };

            Series profitSeries = new Series
            {
                Name = "淨利潤",
                ChartType = SeriesChartType.Line,
                BorderWidth = 3,
                Color = Color.Blue,
                MarkerStyle = MarkerStyle.Diamond,
                MarkerSize = 8,
                ShadowOffset = 0  // 移除陰影效果
            };

            for (int month = 1; month <= 12; month++)
            {
                var monthTransactions = yearTransactions.Where(t => t.Date.Month == month).ToList();
                decimal income = monthTransactions.Where(t => t.Type == TransactionType.收入).Sum(t => t.Amount);
                decimal expense = monthTransactions.Where(t => t.Type == TransactionType.支出).Sum(t => t.Amount);
                decimal profit = income - expense;

                incomeSeries.Points.AddXY($"{month}月", (double)income);
                expenseSeries.Points.AddXY($"{month}月", (double)expense);
                profitSeries.Points.AddXY($"{month}月", (double)profit);
            }

            chart.Series.Add(incomeSeries);
            chart.Series.Add(expenseSeries);
            chart.Series.Add(profitSeries);

            chart.ChartAreas[0].AxisX.Title = "月份";
            chart.ChartAreas[0].AxisY.Title = "金額 (元)";
            chart.ChartAreas[0].AxisX.Interval = 1;
            
            // 優化座標軸標題字體
            chart.ChartAreas[0].AxisX.TitleFont = new Font("Microsoft JhengHei", 10, FontStyle.Bold);
            chart.ChartAreas[0].AxisY.TitleFont = new Font("Microsoft JhengHei", 10, FontStyle.Bold);
        }

        private void AnnualReportForm_Load(object sender, EventArgs e)
        {

        }
    }
}
