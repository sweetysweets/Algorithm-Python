# import java.util.Random;
# public class Main
# {
# private static
# private static
# private static
# final int NUMBER_OF_TESTCASE=60;
# final int NUMBER_OF_OCCURRENCE=1000;
# final String TESTCASE_NAMES[]=new String[]{"向
# 上 1","向上 2","向上 3","向上 4","向上 5","向上 6","向上 7","向下 1","向下 2","向下 3","向下 4","向下 5","向下 6","向下 7","选择楼层 1","选择楼层 2","选择楼层 3","选择楼层 4","选择楼层 5","选择楼层 6","选择楼层 7","选择 楼层 8","选择楼层 9","选择楼层 10","选择楼层 11","选择楼层 12","取消选择 1","取消选择 2","取消选择 3","取消选择 4","取消选择 5","取消选择 6","取消 选择 7","关门 1","关门 2","关门 3","关门 4","关门 5","关门 6","关门 7","延 迟关门 1","延迟关门 2","延迟关门 3","延迟关门 4","延迟关门 5","同时按 1"," 同时按 2","同时按 3","自检 1","自检 2","自检 3","自检 4","自检 5","自检 6", "运行中开门","选择当前楼层","运行中关门","超载报警","不操作 1","不操作 2"};
# private static final int ITERATION_TIMES=1000000; 
# public static void main(String[] args)
# {
# int sequence[]=new int[NUMBER_OF_TESTCASE*NUMBER_OF_OCCURRENCE];
# for(int i=0;i<NUMBER_OF_TESTCASE;i++) for(int j=0;j<NUMBER_OF_OCCURRENCE;j++)
# sequence[NUMBER_OF_OCCURRENCE*i+j]=i; makeRandomSequence(sequence);
# for(int i=0;i<sequence.length;i++)
# System.out.println(TESTCASE_NAMES[sequence[i]]);
# }
# private static void makeRandomSequence(int[] sequence) {
# Random random=new Random();
# int length=sequence.length; for(int i=1;i<=ITERATION_TIMES;i++) {
# int rand1=random.nextInt(length); int rand2=random.nextInt(length);
# int temp=sequence[rand1]; sequence[rand1]=sequence[rand2]; sequence[rand2]=temp;
# } }
# }
#
from _random import Random

NUMBER_OF_TESTCASE=60
NUMBER_OF_OCCURRENCE=1000
TESTCASE_NAMES=["向上 1","向上 2","向上 3","向上 4","向上 5","向上 6","向上 7","向下 1","向下 2","向下 3","向下 4","向下 5","向下 6","向下 7","选择楼层 1","选择楼层 2","选择楼层 3","选择楼层 4","选择楼层 5","选择楼层 6","选择楼层 7","选择 楼层 8","选择楼层 9","选择楼层 10","选择楼层 11","选择楼层 12","取消选择 1","取消选择 2","取消选择 3","取消选择 4","取消选择 5","取消选择 6","取消 选择 7","关门 1","关门 2","关门 3","关门 4","关门 5","关门 6","关门 7","延 迟关门 1","延迟关门 2","延迟关门 3","延迟关门 4","延迟关门 5","同时按 1"," 同时按 2","同时按 3","自检 1","自检 2","自检 3","自检 4","自检 5","自检 6", "运行中开门","选择当前楼层","运行中关门","超载报警","不操作 1","不操作 2"]
ITERATION_TIMES=1000000


def makeRandomSequence(sequence):
    random =Random()
    length=sequence.length
    for i in range(1,ITERATION_TIMES):
        rand1=random.nextInt(length)
        rand2=random.nextInt(length)
        temp=sequence[rand1]
        sequence[rand1]=sequence[rand2]
        sequence[rand2]=temp


if __name__ == '__main__':
    sequence= [0 for i in range(NUMBER_OF_TESTCASE * NUMBER_OF_OCCURRENCE)]
    for i in range(NUMBER_OF_TESTCASE):
        for j in range(NUMBER_OF_OCCURRENCE):
            sequence[NUMBER_OF_OCCURRENCE * i + j] = i
    makeRandomSequence(sequence)
    for i in range(len(sequence)):
        print(TESTCASE_NAMES[sequence[i]])
