using System.Windows.Forms;

namespace WinFormsApp2
{
    internal static class Program
    {
        /// <summary>
        ///  The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main()
        {
            // To customize application configuration such as set high DPI settings or default font,
            // see https://aka.ms/applicationconfiguration.
            ApplicationConfiguration.Initialize();
            
            // 先顯示登入畫面
            LoginForm loginForm = new LoginForm();
            if (loginForm.ShowDialog() == DialogResult.OK)
            {
                // 登入成功，開啟主表單
                Application.Run(new Form1());
            }
            else
            {
                // 登入失敗或取消，結束程式
                Application.Exit();
            }
        }
    }
}