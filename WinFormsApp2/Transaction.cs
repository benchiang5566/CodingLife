using System;
using System.Drawing;

namespace WinFormsApp2
{
    public class Transaction
    {
        public int Id { get; set; }
        public TransactionType Type { get; set; }
        public decimal Amount { get; set; }
        public string Notes { get; set; }
        public Color HighlightColor { get; set; }
        public DateTime Date { get; set; }

        public Transaction()
        {
            Date = DateTime.Now;
            HighlightColor = Color.White;
            Notes = string.Empty;
        }
    }

    public enum TransactionType
    {
        收入,
        支出
    }
}
