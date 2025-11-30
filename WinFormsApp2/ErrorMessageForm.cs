using System;
using System.Drawing;
using System.Windows.Forms;

namespace WinFormsApp2
{
    public partial class ErrorMessageForm : Form
    {
        private Label lblIcon;
        private Label lblMessage;
        private Button btnOK;
        private Panel mainPanel;

        public ErrorMessageForm(string message)
        {
            InitializeComponent();
            SetupUI(message);
        }

        private void InitializeComponent()
        {
            SuspendLayout();
            // 
            // ErrorMessageForm
            // 
            ClientSize = new Size(400, 250);
            Name = "ErrorMessageForm";
            StartPosition = FormStartPosition.CenterParent;
            Text = "µn¤J¥¢±Ñ";
            FormBorderStyle = FormBorderStyle.FixedDialog;
            MaximizeBox = false;
            MinimizeBox = false;
            BackColor = Color.FromArgb(240, 242, 245);
            ResumeLayout(false);
        }

        private void SetupUI(string message)
        {
            // Main panel
            mainPanel = new Panel
            {
                Size = new Size(360, 200),
                Location = new Point(20, 20),
                BackColor = Color.White,
                BorderStyle = BorderStyle.FixedSingle
            };

            // Error icon label
            lblIcon = new Label
            {
                Text = "?",
                Font = new Font("Microsoft JhengHei", 36, FontStyle.Bold),
                ForeColor = Color.FromArgb(204, 0, 0),
                AutoSize = false,
                Size = new Size(80, 80),
                Location = new Point(140, 20),
                TextAlign = ContentAlignment.MiddleCenter
            };

            // Message label
            lblMessage = new Label
            {
                Text = message,
                Font = new Font("Microsoft JhengHei", 11),
                ForeColor = Color.FromArgb(50, 50, 50),
                AutoSize = false,
                Size = new Size(320, 60),
                Location = new Point(20, 100),
                TextAlign = ContentAlignment.MiddleCenter
            };

            // OK button
            btnOK = new Button
            {
                Text = "½T©w",
                Location = new Point(130, 155),
                Size = new Size(100, 35),
                Font = new Font("Microsoft JhengHei", 11, FontStyle.Bold),
                BackColor = Color.FromArgb(204, 0, 0),
                ForeColor = Color.White,
                FlatStyle = FlatStyle.Flat,
                Cursor = Cursors.Hand,
                DialogResult = DialogResult.OK
            };
            btnOK.FlatAppearance.BorderSize = 0;
            btnOK.Click += (s, e) => this.Close();

            // Add controls to main panel
            mainPanel.Controls.AddRange(new Control[]
            {
                lblIcon, lblMessage, btnOK
            });

            // Add main panel to form
            this.Controls.Add(mainPanel);

            // Set accept button
            this.AcceptButton = btnOK;
        }
    }
}
