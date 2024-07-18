"""
This script tests the custom loss function at the utterance and frame levels.
"""

import sys
import os
import unittest
import tensorflow as tf

try:
    from src.training.custom_loss import custom_loss
except ImportError:
    sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
    from src.training.custom_loss import custom_loss


class TestCustomLoss(unittest.TestCase):

    def test_custom_loss_utt(self):
        y_true_utt_1 = tf.constant(
            [[1, 0], [1, 1], [0, 1]], dtype=tf.float32)
        y_pred_utt_1 = tf.constant(
            [[0.9, 0.1], [0.8, 0.2], [0.3, 0.7]], dtype=tf.float32)
        loss_utt_1 = custom_loss(y_true_utt_1, y_pred_utt_1)
        print(f"Utterance-level loss 1: {loss_utt_1}")

        y_true_utt_2 = tf.constant([[1, 1], [1, 1]], dtype=tf.float32)
        y_pred_utt_2 = tf.constant(
            [[0.9, 0.7], [0.8, 0.2]], dtype=tf.float32)
        loss_utt_2 = custom_loss(y_true_utt_2, y_pred_utt_2)
        print(f"Utterance-level loss 2: {loss_utt_2}")

        self.assertAlmostEqual(loss_utt_1, loss_utt_2, places=6)
        print("Utterance-level loss test passed.")

    def test_custom_loss_frame(self):
        y_true_frame_1 = tf.constant(
            [[[1], [0]], [[1], [1]], [[0], [1]]], dtype=tf.float32)
        y_pred_frame_1 = tf.constant([[[0.9], [0.3]], [[0.8], [0.1]], [
            [0.3], [0.7]]], dtype=tf.float32)
        loss_frame_1 = custom_loss(y_true_frame_1, y_pred_frame_1)
        print(f"Frame-level loss 1: {loss_frame_1}")

        y_true_frame_2 = tf.constant(
            [[[1], [1]], [[1], [1]]], dtype=tf.float32)
        y_pred_frame_2 = tf.constant(
            [[[0.9], [0.7]], [[0.8], [0.1]]], dtype=tf.float32)
        loss_frame_2 = custom_loss(y_true_frame_2, y_pred_frame_2)
        print(f"Frame-level loss 2: {loss_frame_2}")

        self.assertAlmostEqual(loss_frame_1, loss_frame_2, places=6)
        print("Frame-level loss test passed.")


if __name__ == "__main__":
    print("Running custom loss tests...")
    unittest.main()