using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using System.Windows.Forms;

namespace WinFormsApp2
{
    public partial class Form1 : Form
    {
        private List<Transaction> transactions = new List<Transaction>();
        private int nextId = 1;

        // UI Controls
        private DataGridView dgvTransactions;
        private ComboBox cmbType;
        private NumericUpDown nudAmount;
        private TextBox txtNotes;
        private Button btnColorPicker;
        private Button btnAdd;
        private Button btnDelete;
        private Button btnAnnualReport;
        private Label lblTotalIncome;
        private Label lblTotalExpense;
        private Label lblNetBalance;
        private Label lblMonthlyProfit;
        private ComboBox cmbMonth;
        private ComboBox cmbYear;
        private Color selectedColor = Color.White;

        public Form1()
        {
            InitializeComponent();
            SetupUI();
            LoadMockData(); // 載入測試資料
            UpdateSummary();
        }

        private void LoadMockData()
        {
            Random random = new Random();
            
            // 收入類別的備註選項
            string[] incomeNotes = new string[]
            {
                "薪資收入",
                "獎金",
                "兼職收入",
                "投資收益",
                "股利收入"
            };
            
            // 支出類別的備註選項
            string[] expenseNotes = new string[]
            {
                "餐飲支出",
                "交通費用",
                "購物消費",
                "水電瓦斯",
                "房租",
                "娛樂支出",
                "醫療費用"
            };
            
            // 顏色選項
            Color[] colors = new Color[]
            {
                Color.LightYellow,
                Color.LightBlue,
                Color.LightGreen,
                Color.LightPink,
                Color.LightCoral,
                Color.LightCyan,
                Color.Lavender,
                Color.White
            };

            // 生成10筆隨機資料
            for (int i = 0; i < 10; i++)
            {
                // 隨機決定是收入還是支出 (30%收入, 70%支出)
                TransactionType type = random.Next(100) < 30 ? TransactionType.收入 : TransactionType.支出;
                
                // 根據類型選擇金額範圍和備註
                decimal amount;
                string note;
                
                if (type == TransactionType.收入)
                {
                    // 收入金額: 20,000 ~ 80,000
                    amount = random.Next(20000, 80001);
                    note = incomeNotes[random.Next(incomeNotes.Length)];
                }
                else
                {
                    // 支出金額: 100 ~ 10,000
                    amount = random.Next(100, 10001);
                    note = expenseNotes[random.Next(expenseNotes.Length)];
                }
                
                // 隨機日期：過去12個月內
                DateTime baseDate = DateTime.Now;
                int daysBack = random.Next(0, 365); // 過去一年內
                DateTime randomDate = baseDate.AddDays(-daysBack);
                
                // 隨機時間
                int randomHour = random.Next(0, 24);
                int randomMinute = random.Next(0, 60);
                randomDate = new DateTime(randomDate.Year, randomDate.Month, randomDate.Day, randomHour, randomMinute, 0);
                
                // 隨機顏色
                Color randomColor = colors[random.Next(colors.Length)];
                
                // 建立交易記錄
                Transaction transaction = new Transaction
                {
                    Id = nextId++,
                    Type = type,
                    Amount = amount,
                    Notes = note,
                    HighlightColor = randomColor,
                    Date = randomDate
                };
                
                transactions.Add(transaction);
            }
            
            // 重新整理顯示
            RefreshGrid();
        }

        private void SetupUI()
        {
            this.Text = "個人記帳系統";
            this.Size = new Size(1200, 700);

            // Left panel for input
            Panel inputPanel = new Panel
            {
                Dock = DockStyle.Left,
                Width = 300,
                Padding = new Padding(10),
                BackColor = Color.FromArgb(240, 240, 240)
            };

            int yPos = 10;

            // Transaction Type
            Label lblType = new Label { Text = "類型:", Location = new Point(10, yPos), AutoSize = true };
            cmbType = new ComboBox
            {
                Location = new Point(10, yPos + 25),
                Width = 260,
                DropDownStyle = ComboBoxStyle.DropDownList
            };
            cmbType.Items.AddRange(new object[] { TransactionType.收入, TransactionType.支出 });
            cmbType.SelectedIndex = 0;

            yPos += 70;

            // Amount
            Label lblAmount = new Label { Text = "金額:", Location = new Point(10, yPos), AutoSize = true };
            nudAmount = new NumericUpDown
            {
                Location = new Point(10, yPos + 25),
                Width = 260,
                Maximum = 999999999,
                DecimalPlaces = 0,
                ThousandsSeparator = true
            };

            yPos += 70;

            // Notes
            Label lblNotes = new Label { Text = "備註:", Location = new Point(10, yPos), AutoSize = true };
            txtNotes = new TextBox
            {
                Location = new Point(10, yPos + 25),
                Width = 260,
                Height = 80,
                Multiline = true,
                ScrollBars = ScrollBars.Vertical
            };

            yPos += 115;

            // Color picker
            Label lblColor = new Label { Text = "標註顏色:", Location = new Point(10, yPos), AutoSize = true };
            btnColorPicker = new Button
            {
                Location = new Point(10, yPos + 25),
                Width = 260,
                Height = 40,
                Text = "選擇顏色",
                BackColor = selectedColor
            };
            btnColorPicker.Click += BtnColorPicker_Click;

            yPos += 75;

            // Add button
            btnAdd = new Button
            {
                Location = new Point(10, yPos),
                Width = 260,
                Height = 40,
                Text = "新增記錄",
                BackColor = Color.FromArgb(0, 122, 204),
                ForeColor = Color.White,
                FlatStyle = FlatStyle.Flat,
                Font = new Font("Microsoft JhengHei", 10, FontStyle.Bold)
            };
            btnAdd.Click += BtnAdd_Click;

            yPos += 50;

            // Delete button
            btnDelete = new Button
            {
                Location = new Point(10, yPos),
                Width = 260,
                Height = 40,
                Text = "刪除選中記錄",
                BackColor = Color.FromArgb(204, 0, 0),
                ForeColor = Color.White,
                FlatStyle = FlatStyle.Flat,
                Font = new Font("Microsoft JhengHei", 10, FontStyle.Bold)
            };
            btnDelete.Click += BtnDelete_Click;

            inputPanel.Controls.AddRange(new Control[] 
            { 
                lblType, cmbType, lblAmount, nudAmount, lblNotes, txtNotes, 
                lblColor, btnColorPicker, btnAdd, btnDelete 
            });

            // Main content panel
            Panel mainPanel = new Panel
            {
                Dock = DockStyle.Fill,
                Padding = new Padding(10)
            };

            // Top panel for summary
            Panel summaryPanel = new Panel
            {
                Dock = DockStyle.Top,
                Height = 150,
                BackColor = Color.White,
                BorderStyle = BorderStyle.FixedSingle
            };

            // Summary labels
            lblTotalIncome = new Label
            {
                Location = new Point(20, 20),
                AutoSize = true,
                Font = new Font("Microsoft JhengHei", 12, FontStyle.Bold),
                ForeColor = Color.Green
            };

            lblTotalExpense = new Label
            {
                Location = new Point(20, 50),
                AutoSize = true,
                Font = new Font("Microsoft JhengHei", 12, FontStyle.Bold),
                ForeColor = Color.Red
            };

            lblNetBalance = new Label
            {
                Location = new Point(20, 80),
                AutoSize = true,
                Font = new Font("Microsoft JhengHei", 14, FontStyle.Bold)
            };

            // Monthly profit calculation
            Label lblMonthlyTitle = new Label
            {
                Text = "月度損益比:",
                Location = new Point(400, 20),
                AutoSize = true,
                Font = new Font("Microsoft JhengHei", 10, FontStyle.Bold)
            };

            cmbYear = new ComboBox
            {
                Location = new Point(400, 50),
                Width = 100,
                DropDownStyle = ComboBoxStyle.DropDownList
            };
            for (int i = DateTime.Now.Year - 5; i <= DateTime.Now.Year + 1; i++)
            {
                cmbYear.Items.Add(i);
            }
            cmbYear.SelectedItem = DateTime.Now.Year;
            cmbYear.SelectedIndexChanged += (s, e) => UpdateMonthlyProfit();

            cmbMonth = new ComboBox
            {
                Location = new Point(510, 50),
                Width = 80,
                DropDownStyle = ComboBoxStyle.DropDownList
            };
            for (int i = 1; i <= 12; i++)
            {
                cmbMonth.Items.Add($"{i}月");
            }
            cmbMonth.SelectedIndex = DateTime.Now.Month - 1;
            cmbMonth.SelectedIndexChanged += (s, e) => UpdateMonthlyProfit();

            lblMonthlyProfit = new Label
            {
                Location = new Point(400, 85),
                AutoSize = true,
                Font = new Font("Microsoft JhengHei", 12, FontStyle.Bold)
            };

            // Annual report button
            btnAnnualReport = new Button
            {
                Location = new Point(650, 45),
                Width = 150,
                Height = 50,
                Text = "年度財報",
                BackColor = Color.FromArgb(46, 125, 50),
                ForeColor = Color.White,
                FlatStyle = FlatStyle.Flat,
                Font = new Font("Microsoft JhengHei", 11, FontStyle.Bold)
            };
            btnAnnualReport.Click += BtnAnnualReport_Click;

            summaryPanel.Controls.AddRange(new Control[] 
            { 
                lblTotalIncome, lblTotalExpense, lblNetBalance,
                lblMonthlyTitle, cmbYear, cmbMonth, lblMonthlyProfit, btnAnnualReport
            });

            // DataGridView for transactions
            dgvTransactions = new DataGridView
            {
                Dock = DockStyle.Fill,
                AutoGenerateColumns = false,
                AllowUserToAddRows = false,
                SelectionMode = DataGridViewSelectionMode.FullRowSelect,
                BackgroundColor = Color.White,
                BorderStyle = BorderStyle.Fixed3D
            };

            dgvTransactions.Columns.Add(new DataGridViewTextBoxColumn { DataPropertyName = "Id", HeaderText = "編號", Width = 60 });
            dgvTransactions.Columns.Add(new DataGridViewTextBoxColumn { DataPropertyName = "Date", HeaderText = "日期", Width = 150, DefaultCellStyle = new DataGridViewCellStyle { Format = "yyyy/MM/dd HH:mm" } });
            dgvTransactions.Columns.Add(new DataGridViewTextBoxColumn { DataPropertyName = "Type", HeaderText = "類型", Width = 80 });
            dgvTransactions.Columns.Add(new DataGridViewTextBoxColumn { DataPropertyName = "Amount", HeaderText = "金額", Width = 120, DefaultCellStyle = new DataGridViewCellStyle { Format = "C0" } });
            dgvTransactions.Columns.Add(new DataGridViewTextBoxColumn { DataPropertyName = "Notes", HeaderText = "備註", AutoSizeMode = DataGridViewAutoSizeColumnMode.Fill });

            dgvTransactions.CellFormatting += DgvTransactions_CellFormatting;

            mainPanel.Controls.Add(dgvTransactions);
            mainPanel.Controls.Add(summaryPanel);

            this.Controls.Add(mainPanel);
            this.Controls.Add(inputPanel);
        }

        private void BtnColorPicker_Click(object sender, EventArgs e)
        {
            using (ColorDialog colorDialog = new ColorDialog())
            {
                colorDialog.Color = selectedColor;
                if (colorDialog.ShowDialog() == DialogResult.OK)
                {
                    selectedColor = colorDialog.Color;
                    btnColorPicker.BackColor = selectedColor;
                }
            }
        }

        private void BtnAdd_Click(object sender, EventArgs e)
        {
            if (nudAmount.Value <= 0)
            {
                MessageBox.Show("請輸入有效金額！", "錯誤", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                return;
            }

            Transaction transaction = new Transaction
            {
                Id = nextId++,
                Type = (TransactionType)cmbType.SelectedItem,
                Amount = nudAmount.Value,
                Notes = txtNotes.Text,
                HighlightColor = selectedColor,
                Date = DateTime.Now
            };

            transactions.Add(transaction);
            RefreshGrid();
            UpdateSummary();

            // Reset form
            nudAmount.Value = 0;
            txtNotes.Clear();
            selectedColor = Color.White;
            btnColorPicker.BackColor = selectedColor;

            MessageBox.Show("記錄已新增！", "成功", MessageBoxButtons.OK, MessageBoxIcon.Information);
        }

        private void BtnDelete_Click(object sender, EventArgs e)
        {
            if (dgvTransactions.SelectedRows.Count == 0)
            {
                MessageBox.Show("請選擇要刪除的記錄！", "提示", MessageBoxButtons.OK, MessageBoxIcon.Information);
                return;
            }

            if (MessageBox.Show("確定要刪除選中的記錄嗎？", "確認", MessageBoxButtons.YesNo, MessageBoxIcon.Question) == DialogResult.Yes)
            {
                foreach (DataGridViewRow row in dgvTransactions.SelectedRows)
                {
                    int id = (int)row.Cells[0].Value;
                    transactions.RemoveAll(t => t.Id == id);
                }

                RefreshGrid();
                UpdateSummary();
                MessageBox.Show("記錄已刪除！", "成功", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
        }

        private void BtnAnnualReport_Click(object sender, EventArgs e)
        {
            AnnualReportForm reportForm = new AnnualReportForm(transactions);
            reportForm.ShowDialog();
        }

        private void RefreshGrid()
        {
            dgvTransactions.DataSource = null;
            dgvTransactions.DataSource = transactions.OrderByDescending(t => t.Date).ToList();
        }

        private void UpdateSummary()
        {
            decimal totalIncome = transactions.Where(t => t.Type == TransactionType.收入).Sum(t => t.Amount);
            decimal totalExpense = transactions.Where(t => t.Type == TransactionType.支出).Sum(t => t.Amount);
            decimal netBalance = totalIncome - totalExpense;

            lblTotalIncome.Text = $"總收入: {totalIncome:C0}";
            lblTotalExpense.Text = $"總支出: {totalExpense:C0}";
            lblNetBalance.Text = $"淨餘額: {netBalance:C0}";
            lblNetBalance.ForeColor = netBalance >= 0 ? Color.DarkGreen : Color.DarkRed;

            UpdateMonthlyProfit();
        }

        private void UpdateMonthlyProfit()
        {
            if (cmbYear.SelectedItem == null || cmbMonth.SelectedItem == null) return;

            int year = (int)cmbYear.SelectedItem;
            int month = cmbMonth.SelectedIndex + 1;

            var monthlyTransactions = transactions.Where(t => t.Date.Year == year && t.Date.Month == month).ToList();
            decimal monthlyIncome = monthlyTransactions.Where(t => t.Type == TransactionType.收入).Sum(t => t.Amount);
            decimal monthlyExpense = monthlyTransactions.Where(t => t.Type == TransactionType.支出).Sum(t => t.Amount);
            decimal monthlyProfit = monthlyIncome - monthlyExpense;

            if (monthlyIncome + monthlyExpense == 0)
            {
                lblMonthlyProfit.Text = "損益: 無資料";
                lblMonthlyProfit.ForeColor = Color.Gray;
            }
            else
            {
                decimal profitRatio = monthlyExpense != 0 ? (monthlyProfit / monthlyExpense) * 100 : 0;
                lblMonthlyProfit.Text = $"損益: {monthlyProfit:C0} (比率: {profitRatio:F2}%)";
                lblMonthlyProfit.ForeColor = monthlyProfit >= 0 ? Color.Green : Color.Red;
            }
        }

        private void DgvTransactions_CellFormatting(object sender, DataGridViewCellFormattingEventArgs e)
        {
            if (e.RowIndex >= 0 && e.RowIndex < transactions.Count)
            {
                var transaction = ((List<Transaction>)dgvTransactions.DataSource)[e.RowIndex];
                dgvTransactions.Rows[e.RowIndex].DefaultCellStyle.BackColor = transaction.HighlightColor;

                // Set text color based on background brightness
                int brightness = (int)((transaction.HighlightColor.R * 0.299) + 
                                      (transaction.HighlightColor.G * 0.587) + 
                                      (transaction.HighlightColor.B * 0.114));
                dgvTransactions.Rows[e.RowIndex].DefaultCellStyle.ForeColor = brightness > 128 ? Color.Black : Color.White;
            }
        }
    }
}
