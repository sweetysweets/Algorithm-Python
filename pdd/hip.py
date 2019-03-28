# 第三题 二维生物的旅行
#
# 二维生物hip当前处于x轴的0坐标位置，打算去拜访它的老友hop，hop位于坐标轴的target位置。hip有一个很奇怪的能力，其迈出的第n步（从1算起），步长为n。也就是说第一步可以移动的距离为1，第二步可以移动的距离为2，以此类推。每走一步之前，hip都可以决定这一步是向左走还是向右走，但每一步都只能朝一个方向前进。二维生物都很懒，hip希望你能先帮他计算出最少需要走多少步才能到达target位置，他再决定要不要去拜访老友。
#
# 输入描述：
#
# 每个测试输入包含1个测试用例，即给出目标位置target的值。这里保证-10^9<=target<=10^9,且为整数


# public static int test3(int target){
#         int n=Math.abs(target);
#         int k=(int)Math.ceil((Math.sqrt(8*n+1)-1)/2);
#         int total=k*(k+1)/2;
#         int d=total-n;
#         if(d%2==0)
#             return k;
#         else if(d+k+1%2==0)
#             return k+1;
#         else
#             return k+2;
#     }


# 字符串构造
#
# 有一个长度为n的字符串P，我们可以通过P构造出一个无限长度的字符串S, 其中S[i] = P[i % n]。
# 给定一个字符串S，求可以通过上述方法构造出S的最短字符串P。
#
# public
# static
# void
# test2(String
# s){
#
# for (int i=1;i < s.length();i++){
# String str=s.substring(0, i);
# StringBuffer temp=new StringBuffer("");
# for (int j=0;j < s.length() / i;j++)
# temp.append(str);
# temp.append(s.substring(0, s.length() % i));
# if (temp.toString().equals(s)) {
# System.out.println(str);
# break;
# }
# }
# }


# 4靓号
#
# A国手机号码由且仅由N位十进制数值(0-9)组成。一个手机号码中有至少K位数字相同则被定义为靓号。
# A国的手机号可以有前导零，比如000123456是一个合法的手机号。小多想花钱将自己的手机号码修改为一个靓号。
# 修改号码中一个数字需要花费的金额为新数字与旧数字之间的差值。比如将1修改为6或6修改为1都需要花5块钱。
# 给出小多现在的手机号码，问将其修改成一个靓号，最少需要多少钱？
#
# 输入描述：
#
# 第一行包含两个整数N，K，分别表示手机号码数字个数以及靓号至少有K个数字相同。
#
# 第二行包含N个字符，每个字符都是一个数字，数字之间没有任何其他空白符。表示小多的手机号码。
#
# 数据范围2<=K<=N<=10000
#
# 输出描述：
#
# 第一行包含一个整数，表示修改成一个靓号，最少需要的金额。
#
# 第二行包含N个数字字符，表示最少花费修改的新手机号。若有多个靓号花费都最少，则输出字典序最小的靓号。

#
# public
# static
# void
# test4()
# {
#     Scanner
# scanner = new
# Scanner(System. in);
# int
# N = scanner.nextInt();
# int
# K = scanner.nextInt();
# String
# s = scanner.next();
# StringBuffer
# ans = null;
# int
# res = (int)
# 1e9;
# for (int i=0;i < 10;i++)
# {
#     StringBuffer
# t = new
# StringBuffer(s);
# int
# p = K, c = 0;
# for (int j=0;j < 10;j++)
# {
# for (int l=0;l < N;l++){
# if (p != 0 & & t.charAt(l) - '0' == i + j){
# p--;
# t.setCharAt(l, (char)(i+'0'));
# c=c+j;
# }
# }
# if (j != 0)
# for (int l=N-1;l >= 0;l--)
# if (p != 0 & & t.charAt(l)-'0' == i-j){
# p--;
# t.setCharAt(l, (char)(i+'0'));
# c=c+j;
# }
# }
# if (c < res){
# res=c;
# ans=t;
# }
#
# }
# System.out.println(res);
# System.out.println(ans);
# }解题思路：

# 1）对于给定的k,分别求得相同个数满足看，数字为0-9分别所需要的花费，最小的就是答案。
#
# 2）对于变换成指定数字，有很多种方法，哪一种最小呢？就是先从当前数字最近的开始找，
# 比如 13245 变换成至少3个1，
# 那么先找离数字1最近的，距离为1或者-1的数字2，
# 此时k还不满足要求，在找距离为2的数字3，此时满足幸运数字定义。得到花费c。
#3）对于2），很明显那是花费最小的搜索路径。