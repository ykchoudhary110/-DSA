class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        # ---------------------------------------------------------
        # This dictionary will store our final groups.
        #
        # KEY   = frequency pattern of a word
        # VALUE = list of words having that same frequency pattern
        #
        # For example:
        #
        # "eat", "tea", "ate"
        #
        # all have:
        # a -> 1
        # e -> 1
        # t -> 1
        #
        # Therefore, they will have the same KEY and go
        # into the same list.
        # ---------------------------------------------------------
        groups = {}


        # ---------------------------------------------------------
        # Process every word one by one.
        #
        # Example:
        # strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        #
        # First:
        # word = "eat"
        #
        # Then:
        # word = "tea"
        #
        # Then:
        # word = "tan"
        #
        # ...and so on.
        # ---------------------------------------------------------
        for word in strs:

            # -----------------------------------------------------
            # Create a frequency array of size 26.
            #
            # Why 26?
            #
            # The problem contains lowercase English letters only:
            #
            # a, b, c, d, ... z
            #
            # So we need exactly 26 positions.
            #
            # Each position represents one character:
            #
            # index 0  -> a
            # index 1  -> b
            # index 2  -> c
            # ...
            # index 25 -> z
            #
            # Initially every count is 0.
            #
            # [0, 0, 0, 0, ... 0]   (26 zeros)
            # -----------------------------------------------------
            freq = [0] * 26


            # -----------------------------------------------------
            # Now go through every character of the current word.
            #
            # We are using the SAME frequency-counting idea that
            # you learned earlier:
            #
            #     freq[s[right]] = freq.get(s[right], 0) + 1
            #
            # But here we are using an array instead of a dictionary.
            #
            # 'right' represents the current character's index.
            # -----------------------------------------------------
            for right in range(len(word)):

                # -------------------------------------------------
                # We need to convert the character into a number
                # from 0 to 25.
                #
                # ord() gives the numerical Unicode value of a
                # character.
                #
                # For example:
                #
                # ord('a') = 97
                # ord('b') = 98
                # ord('c') = 99
                #
                # Therefore:
                #
                # ord('a') - ord('a') = 0
                # ord('b') - ord('a') = 1
                # ord('c') - ord('a') = 2
                #
                # So:
                #
                # a -> index 0
                # b -> index 1
                # c -> index 2
                # ...
                # z -> index 25
                #
                # Example:
                #
                # word[right] = 'e'
                #
                # ord('e') - ord('a')
                # = 101 - 97
                # = 4
                #
                # So 'e' uses freq[4].
                # -------------------------------------------------
                freq[ord(word[right]) - ord('a')] += 1


            # -----------------------------------------------------
            # At this point, 'freq' contains the complete frequency
            # of every character in the current word.
            #
            # For example:
            #
            # word = "eat"
            #
            # frequency is:
            #
            # a -> 1
            # e -> 1
            # t -> 1
            #
            # The frequency array represents exactly this pattern.
            #
            # We convert the list into a tuple because a LIST
            # cannot be used as a dictionary key, but a TUPLE can.
            #
            # So:
            #
            # freq = [1, 0, 0, ..., 1, ..., 1, ...]
            #
            # becomes:
            #
            # key = (1, 0, 0, ..., 1, ..., 1, ...)
            #
            # This KEY uniquely represents the character frequencies.
            # -----------------------------------------------------
            key = tuple(freq)


            # -----------------------------------------------------
            # Now check whether this frequency pattern already exists
            # in our dictionary.
            #
            # If it does NOT exist, create an empty list for it.
            #
            # Example:
            #
            # First word = "eat"
            #
            # Its key represents:
            # a -> 1
            # e -> 1
            # t -> 1
            #
            # This key doesn't exist yet, so create:
            #
            # groups[key] = []
            # -----------------------------------------------------
            if key not in groups:
                groups[key] = []


            # -----------------------------------------------------
            # Now put the ORIGINAL word into its group.
            #
            # For example:
            #
            # word = "eat"
            #
            # groups[key] becomes:
            #
            # ["eat"]
            #
            # Later, when we process "tea", it produces the EXACT
            # SAME frequency key.
            #
            # Therefore "tea" goes into the SAME list:
            #
            # ["eat", "tea"]
            #
            # Then "ate":
            #
            # ["eat", "tea", "ate"]
            # -----------------------------------------------------
            groups[key].append(word)


        # ---------------------------------------------------------
        # At this point, the dictionary contains something like:
        #
        # {
        #     frequency_pattern_1: ["eat", "tea", "ate"],
        #     frequency_pattern_2: ["tan", "nat"],
        #     frequency_pattern_3: ["bat"]
        # }
        #
        # We don't need the frequency keys anymore.
        #
        # We only want the groups.
        #
        # groups.values() gives us:
        #
        # ["eat", "tea", "ate"]
        # ["tan", "nat"]
        # ["bat"]
        #
        # list() converts those dictionary values into the required
        # list of lists.
        # ---------------------------------------------------------
        return list(groups.values())