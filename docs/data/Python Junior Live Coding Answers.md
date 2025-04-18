# Python Junior Live Coding Answers

## Live Coding Answers (Pages 16-17)

 1. `print("Hello, World!")`
 2. `def add(a, b): return a + b`
 3. `numbers = [1, 2, 3, 4, 5]; print(numbers)`
 4. `numbers = [3, 1, 4, 2]; numbers.sort()`
 5. `def is_even(num): return num % 2 == 0`
 6. `my_dict = {'a': 1, 'b': 2, 'c': 3}; print(my_dict)`
 7. `string = input(); print(len(string))`
 8. `def max_item(lst): return max(lst)`
 9. `my_tuple = (1, 2, 3); print(my_tuple)`
10. `def fibonacci(n): a, b = 0, 1; for _ in range(n): print(a); a, b = b, a + b`
11. `def safe_divide(a, b): try: return a / b except ZeroDivisionError: return "Деление на ноль!"`
12. `def square(num): return num ** 2`
13. `my_list = [1, 2, 3]; count = len(my_list)`
14. `num = 123; result = str(num)`
15. `def even_elements(lst): return [x for x in lst if x % 2 == 0]`
16. `def is_empty(string): return not string`
17. `squares = [x**2 for x in range(1, 11)]`
18. `def first_item(lst): return lst[0] if lst else None`
19. `dict1 = {'a': 1, 'b': 2}; dict2 = {'c': 3}; merged_dict = {**dict1, **dict2}`
20. `def string_lengths(lst): return [len(s) for s in lst]`
21. `def reverse_string(s): return s[::-1]`
22. `def find_index(lst, value): return lst.index(value) if value in lst else -1`
23. `evens = [x for x in range(1, 21) if x % 2 == 0]`
24. `def sum_list(lst): return sum(lst)`
25. `names = ["Alice", "Bob", "Charlie"]; name_lengths = {name: len(name) for name in names}`
26. 

def is_prime(n): if n &lt; 2: return False for i in range(2, int(n\*\*0.5) + 1): if n % i == 0: return False return True

```
27. `def remove_duplicates(lst): return list(set(lst))`
28. `def to_upper(string): return string.upper()`
29. `def count_vowels(s): vowels = "aeiouAEIOU"; return sum(1 for char in s if char in vowels)`
30. `def last_item(lst): return lst[-1] if lst else None`
31. `def common_elements(list1, list2): return list(set(list1) & set(list2))`
32. `def multiply(a, b): return a * b`
33. `def unique_letters(s): return list(set(s))`
34. `def max_value(d): return max(d.values()) if d else None`
35. `def is_anagram(s1, s2): return sorted(s1) == sorted(s2)`
```