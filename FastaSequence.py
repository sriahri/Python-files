class MotifScanner:
    # Declares the class MotifScanner
    def __init__(self, sequence, tfbs):
        # Initializes the class
        # sequence: stores the DNA sequence
        # tbfs: dictionary containing the transcription factor binding site patterns
        if not isinstance(sequence, str) or not isinstance(tfbs, dict):
            raise TypeError("sequence should be a string and tfbs should be a dict.")
        self.sequence = sequence
        self.tfbs = tfbs

    def findmotifs(self, tf):
        #  find motifs associated with a specific transcription factor within the provided DNA sequence
        if not isinstance(tf, str):
            raise TypeError("tf should be a string.")
        if tf not in self.tfbs:
            raise ValueError("TF not found!")
        tss_position = len(self.sequence) // 2
        tf_occurrences = re.findall(self.tfbs[tf], self.sequence)
        return {pos - tss_position: motif for pos, motif in enumerate(tf_occurrences, start=1)}
