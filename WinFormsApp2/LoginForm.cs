using System;
using System.Drawing;
using System.Windows.Forms;

namespace WinFormsApp2
{
    public partial class LoginForm : Form
    {
        private static string currentUsername = "admin";
        private static string currentPassword = "1234";

        private TextBox txtUsername;
        private TextBox txtPassword;
        private Button btnLogin;
        private Button btnForgotPassword;
        private Button btnTogglePassword;
        private CheckBox chkShowPassword;
        private Label lblTitle;
        private Label lblUsername;
        private Label lblPassword;
        private Panel mainPanel;

        public LoginForm()
        {
            InitializeComponent();
            SetupUI();
        }

        private void InitializeComponent()
        {
            SuspendLayout();
            // 
            // LoginForm
            // 
            ClientSize = new Size(450, 550);
            Name = "LoginForm";
            StartPosition = FormStartPosition.CenterScreen;
            Text = "系統登入";
            FormBorderStyle = FormBorderStyle.FixedDialog;
            MaximizeBox = false;
            BackColor = Color.FromArgb(240, 242, 245);
            ResumeLayout(false);
        }

        private void SetupUI()
        {
            // Main panel
            mainPanel = new Panel
            {
                Size = new Size(380, 450),
                Location = new Point(35, 40),
                BackColor = Color.White,
                BorderStyle = BorderStyle.FixedSingle
            };

            // Title
            lblTitle = new Label
            {
                Text = "個人記帳系統",
                Font = new Font("Microsoft JhengHei", 20, FontStyle.Bold),
                ForeColor = Color.FromArgb(0, 122, 204),
                AutoSize = false,
                Size = new Size(340, 50),
                Location = new Point(20, 30),
                TextAlign = ContentAlignment.MiddleCenter
            };

            // Subtitle
            Label lblSubtitle = new Label
            {
                Text = "請輸入您的帳號和密碼",
                Font = new Font("Microsoft JhengHei", 10),
                ForeColor = Color.Gray,
                AutoSize = false,
                Size = new Size(340, 30),
                Location = new Point(20, 85),
                TextAlign = ContentAlignment.MiddleCenter
            };

            // Username label
            lblUsername = new Label
            {
                Text = "帳號:",
                Font = new Font("Microsoft JhengHei", 11, FontStyle.Bold),
                Location = new Point(30, 140),
                AutoSize = true
            };

            // Username textbox
            txtUsername = new TextBox
            {
                Location = new Point(30, 170),
                Size = new Size(320, 35),
                Font = new Font("Microsoft JhengHei", 12),
                PlaceholderText = "請輸入帳號"
            };

            // Password label
            lblPassword = new Label
            {
                Text = "密碼:",
                Font = new Font("Microsoft JhengHei", 11, FontStyle.Bold),
                Location = new Point(30, 225),
                AutoSize = true
            };

            // Password textbox
            txtPassword = new TextBox
            {
                Location = new Point(30, 255),
                Size = new Size(320, 35),
                Font = new Font("Microsoft JhengHei", 12),
                UseSystemPasswordChar = true,
                PlaceholderText = "請輸入密碼"
            };
            txtPassword.KeyPress += TxtPassword_KeyPress;

            // Show password checkbox
            chkShowPassword = new CheckBox
            {
                Text = "顯示密碼",
                Location = new Point(30, 300),
                AutoSize = true,
                Font = new Font("Microsoft JhengHei", 9)
            };
            chkShowPassword.CheckedChanged += ChkShowPassword_CheckedChanged;

            // Login button
            btnLogin = new Button
            {
                Text = "登入",
                Location = new Point(30, 345),
                Size = new Size(320, 45),
                Font = new Font("Microsoft JhengHei", 12, FontStyle.Bold),
                BackColor = Color.FromArgb(0, 122, 204),
                ForeColor = Color.White,
                FlatStyle = FlatStyle.Flat,
                Cursor = Cursors.Hand
            };
            btnLogin.FlatAppearance.BorderSize = 0;
            btnLogin.Click += BtnLogin_Click;

            // Forgot password button
            btnForgotPassword = new Button
            {
                Text = "忘記密碼?",
                Location = new Point(125, 400),
                Size = new Size(130, 30),
                Font = new Font("Microsoft JhengHei", 9),
                BackColor = Color.Transparent,
                ForeColor = Color.FromArgb(0, 122, 204),
                FlatStyle = FlatStyle.Flat,
                Cursor = Cursors.Hand
            };
            btnForgotPassword.FlatAppearance.BorderSize = 0;
            btnForgotPassword.Click += BtnForgotPassword_Click;

            // Add controls to main panel     
            mainPanel.Controls.AddRange(new Control[]
            {
                lblTitle, lblSubtitle, lblUsername, txtUsername,
                lblPassword, txtPassword, chkShowPassword,
                btnLogin, btnForgotPassword
            });

            // Add main panel to form
            this.Controls.Add(mainPanel);

            // Set default focus
            this.AcceptButton = btnLogin;
        }

        private void ChkShowPassword_CheckedChanged(object sender, EventArgs e)
        {
            txtPassword.UseSystemPasswordChar = !chkShowPassword.Checked;
        }

        private void TxtPassword_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (e.KeyChar == (char)Keys.Enter)
            {
                BtnLogin_Click(sender, e);
            }
        }

        private void BtnLogin_Click(object sender, EventArgs e)
        {
            string username = txtUsername.Text.Trim();
            string password = txtPassword.Text;

            // 驗證輸入
            if (string.IsNullOrEmpty(username) || string.IsNullOrEmpty(password))
            {
                ShowErrorMessage("帳號和密碼不能為空!");
                return;
            }

            // 驗證帳號密碼
            if (username == currentUsername && password == currentPassword)
            {
                // 登入成功
                this.DialogResult = DialogResult.OK;
                this.Close();
            }
            else
            {
                // 登入失敗
                ShowErrorMessage("帳號或密碼輸入錯誤!\n\n請檢查您的帳號和密碼。");
                txtPassword.Clear();
                txtPassword.Focus();
            }
        }

        private void BtnForgotPassword_Click(object sender, EventArgs e)
        {
            ResetPasswordForm resetForm = new ResetPasswordForm();
            if (resetForm.ShowDialog() == DialogResult.OK)
            {
                // 更新帳號密碼
                currentUsername = resetForm.NewUsername;
                currentPassword = resetForm.NewPassword;

                MessageBox.Show("帳號和密碼已成功重設!\n\n新帳號: " + currentUsername,
                    "重設成功",
                    MessageBoxButtons.OK,
                    MessageBoxIcon.Information);

                // 清空輸入欄位
                txtUsername.Clear();
                txtPassword.Clear();
                txtUsername.Focus();
            }
        }

        private void ShowErrorMessage(string message)
        {
            ErrorMessageForm errorForm = new ErrorMessageForm(message);
            errorForm.ShowDialog();
        }

        // 靜態方法供外部重設密碼使用
        public static void UpdateCredentials(string username, string password)
        {
            currentUsername = username;
            currentPassword = password;
        }
    }
}
