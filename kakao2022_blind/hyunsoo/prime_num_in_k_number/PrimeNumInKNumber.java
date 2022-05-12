package kakao2022_blind.prime_num_in_k_number;

class Solution {
    boolean check(long num) {
        if (num == 2)
            return true;
        if (num == 1 || num % 2 == 0)
            return false;

        for (long i = 3; i <= (long) Math.sqrt(num); i += 2) {
            if (num % i == 0)
                return false;
        }

        return true;
    }

    String convert(int num, int base) {
        int q = num / base, r = num % base;
        if (q != 0)
            return convert(q, base) + String.valueOf(r);
        else
            return String.valueOf(r);
    }

    public int solution(int n, int k) {
        String number = k == 10 ? String.valueOf(n) : convert(n, k);
        String[] nums = number.split("0+"); // 0 한 개 이상으로 구별, 빈 문자열 안 들어감

        int answer = 0;
        for (String value : nums) {
            if (check(Long.parseLong(value)))
                answer++;
        }
        return answer;
    }
}

public class PrimeNumInKNumber {
    public static void main(String[] args) {
        Solution so = new Solution();
        System.out.println(so.solution(437674, 3));
    }
}
