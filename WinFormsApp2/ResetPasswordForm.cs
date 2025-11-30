using System;
using System.Drawing;
using System.Windows.Forms;

namespace WinFormsApp2
{
    public partial class ResetPasswordForm : Form
    {
        private TextBox txtNewUsername;
        private TextBox txtNewPassword;
        private TextBox txtConfirmPassword;
        private Button btnReset;
        private Button btnCancel;
        private Label lblTitle;
        private Label lblUsername;
        private Label lblPassword;
        private Label lblConfirmPassword;
        private CheckBox chkShowPassword;
        private Panel mainPanel;

        public string NewUsername { get; private set; }
        public string NewPassword { get; private set; }

        public ResetPasswordForm()
        {
            InitializeComponent();
            SetupUI();
        }

        private void InitializeComponent()
        {
            SuspendLayout();
            // 
            // ResetPasswordForm
            // 
            ClientSize = new Size(450, 550);
            Name = "ResetPasswordForm";
            StartPosition = FormStartPosition.CenterParent;
            Text = "重設帳號密碼";
            FormBorderStyle = FormBorderStyle.FixedDialog;
            MaximizeBox = false;
            MinimizeBox = false;
            BackColor = Color.FromArgb(240, 242, 245);
            ResumeLayout(false);
        }

        private void SetupUI()
        {
            // Main panel
            mainPanel = new Panel
            {
                Size = new Size(380, 480),
                Location = new Point(35, 30),
                BackColor = Color.White,
                BorderStyle = BorderStyle.FixedSingle
            };

            // Title
            lblTitle = new Label
            {
                Text = "重設帳號密碼",
                Font = new Font("Microsoft JhengHei", 18, FontStyle.Bold),
                ForeColor = Color.FromArgb(46, 125, 50),
                AutoSize = false,
                Size = new Size(340, 50),
                Location = new Point(20, 30),
                TextAlign = ContentAlignment.MiddleCenter
            };

            // Info label
            Label lblInfo = new Label
            {
                Text = "請輸入新的帳號和密碼\n設定後將覆蓋原有的登入資訊",
                Font = new Font("Microsoft JhengHei", 9),
                ForeColor = Color.Gray,
                AutoSize = false,
                Size = new Size(340, 45),
                Location = new Point(20, 85),
                TextAlign = ContentAlignment.MiddleCenter
            };

            // Username label
            lblUsername = new Label
            {
                Text = "新帳號:",
                Font = new Font("Microsoft JhengHei", 11, FontStyle.Bold),
                Location = new Point(30, 150),
                AutoSize = true
            };

            // Username textbox
            txtNewUsername = new TextBox
            {
                Location = new Point(30, 180),
                Size = new Size(320, 35),
                Font = new Font("Microsoft JhengHei", 12),
                PlaceholderText = "請輸入新帳號"
            };

            // Password label
            lblPassword = new Label
            {
                Text = "新密碼:",
                Font = new Font("Microsoft JhengHei", 11, FontStyle.Bold),
                Location = new Point(30, 235),
                AutoSize = true
            };

            // Password textbox
            txtNewPassword = new TextBox
            {
                Location = new Point(30, 265),
                Size = new Size(320, 35),
                Font = new Font("Microsoft JhengHei", 12),
                UseSystemPasswordChar = true,
                PlaceholderText = "請輸入新密碼"
            };

            // Confirm password label
            lblConfirmPassword = new Label
            {
                Text = "確認密碼:",
                Font = new Font("Microsoft JhengHei", 11, FontStyle.Bold),
                Location = new Point(30, 320),
                AutoSize = true
            };

            // Confirm password textbox
            txtConfirmPassword = new TextBox
            {
                Location = new Point(30, 350),
                Size = new Size(320, 35),
                Font = new Font("Microsoft JhengHei", 12),
                UseSystemPasswordChar = true,
                PlaceholderText = "請再次輸入密碼"
            };

            // Show password checkbox
            chkShowPassword = new CheckBox
            {
                Text = "顯示密碼",
                Location = new Point(30, 395),
                AutoSize = true,
                Font = new Font("Microsoft JhengHei", 9)
            };
            chkShowPassword.CheckedChanged += ChkShowPassword_CheckedChanged;

            // Reset button
            btnReset = new Button
            {
                Text = "確認重設",
                Location = new Point(30, 425),
                Size = new Size(155, 40),
                Font = new Font("Microsoft JhengHei", 11, FontStyle.Bold),
                BackColor = Color.FromArgb(46, 125, 50),
                ForeColor = Color.White,
                FlatStyle = FlatStyle.Flat,
                Cursor = Cursors.Hand
            };
            btnReset.FlatAppearance.BorderSize = 0;
            btnReset.Click += BtnReset_Click;

            // Cancel button
            btnCancel = new Button
            {
                Text = "取消",
                Location = new Point(195, 425),
                Size = new Size(155, 40),
                Font = new Font("Microsoft JhengHei", 11, FontStyle.Bold),
                BackColor = Color.Gray,
                ForeColor = Color.White,
                FlatStyle = FlatStyle.Flat,
                Cursor = Cursors.Hand
            };
            btnCancel.FlatAppearance.BorderSize = 0;
            btnCancel.Click += BtnCancel_Click;

            // Add controls to main panel
            mainPanel.Controls.AddRange(new Control[]
            {
                lblTitle, lblInfo, lblUsername, txtNewUsername,
                lblPassword, txtNewPassword, lblConfirmPassword, txtConfirmPassword,
                chkShowPassword, btnReset, btnCancel
            });

            // Add main panel to form
            this.Controls.Add(mainPanel);
        }

        private void ChkShowPassword_CheckedChanged(object sender, EventArgs e)
        {
            txtNewPassword.UseSystemPasswordChar = !chkShowPassword.Checked;
            txtConfirmPassword.UseSystemPasswordChar = !chkShowPassword.Checked;
        }

        private void BtnReset_Click(object sender, EventArgs e)
        {
            string username = txtNewUsername.Text.Trim();
            string password = txtNewPassword.Text;
            string confirmPassword = txtConfirmPassword.Text;

            // 驗證輸入
            if (string.IsNullOrEmpty(username))
            {
                MessageBox.Show("帳號不能為空!",
                    "輸入錯誤",
                    MessageBoxButtons.OK,
                    MessageBoxIcon.Warning);
                txtNewUsername.Focus();
                return;
            }

            if (username.Length < 3)
            {
                MessageBox.Show("帳號長度至少需要3個字元!",
                    "輸入錯誤",
                    MessageBoxButtons.OK,
                    MessageBoxIcon.Warning);
                txtNewUsername.Focus();
                return;
            }

            if (string.IsNullOrEmpty(password))
            {
                MessageBox.Show("密碼不能為空!",
                    "輸入錯誤",
                    MessageBoxButtons.OK,
                    MessageBoxIcon.Warning);
                txtNewPassword.Focus();
                return;
            }

            if (password.Length < 4)
            {
                MessageBox.Show("密碼長度至少需要4個字元!",
                    "輸入錯誤",
                    MessageBoxButtons.OK,
                    MessageBoxIcon.Warning);
                txtNewPassword.Focus();
                return;
            }

            if (password != confirmPassword)
            {
                MessageBox.Show("兩次輸入的密碼不一致!\n\n請重新輸入。",
                    "密碼不符",
                    MessageBoxButtons.OK,
                    MessageBoxIcon.Warning);
                txtConfirmPassword.Clear();
                txtNewPassword.Clear();
                txtNewPassword.Focus();
                return;
            }

            // 確認重設
            DialogResult result = MessageBox.Show(
                $"確認要將帳號密碼重設為:\n\n帳號: {username}\n密碼: {new string('*', password.Length)}\n\n此操作將覆蓋原有的登入資訊!",
                "確認重設",
                MessageBoxButtons.YesNo,
                MessageBoxIcon.Question);

            if (result == DialogResult.Yes)
            {
                NewUsername = username;
                NewPassword = password;
                this.DialogResult = DialogResult.OK;
                this.Close();
            }
        }

        private void BtnCancel_Click(object sender, EventArgs e)
        {
            this.DialogResult = DialogResult.Cancel;
            this.Close();
        }
    }
}
