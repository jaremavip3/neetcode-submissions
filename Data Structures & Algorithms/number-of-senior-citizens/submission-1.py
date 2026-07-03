class Solution:
    def countSeniors(self, details: List[str]) -> int:
        result = 0;
        for detail in details:
            details_char_array = list(detail)
            pass_age = int(details_char_array[11] + details_char_array[12])
            if(pass_age > 60):
                result += 1;
        return result;
