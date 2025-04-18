// week09_5_bubble_happy_part1

size(310,430);
strokeWeight(3);
fill(255,255,0);
rect(10, 10, 58*5, 58*7, 30);
for(int i=10+58; i<10+58*7; i+=58){
  line(10, i, 300, i);
  
}
for(int i=0; i<7; i++){ // 左手 i 有 7 個
  for(int j=0; j<5; j++){ //右手 j 有 5 個
    int x= 39+j*58, y=39+i*58; // x 對應右手 j y 左手 i
    ellipse(x, y, 50, 50);
  }
}
