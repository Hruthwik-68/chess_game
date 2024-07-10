# models.py
import chess
import chess.engine
from django.db import models

class ChessGame(models.Model):
    fen = models.CharField(max_length=100, default=chess.STARTING_FEN)

    def move_white(self):
        board = chess.Board(self.fen)
        engine_path = r'C:\Users\POOJA\Downloads\stockfish-windows-x86-64-avx2\stockfish\stockfish-windows-x86-64-avx2.exe'
        engine = chess.engine.SimpleEngine.popen_uci(engine_path)
        result = engine.play(board, chess.engine.Limit(time=0.1))
        move = result.move
        board.push(move)
        self.fen = board.fen()
        self.save()
        engine.quit()
        return move.uci()

    def move_black(self):
        board = chess.Board(self.fen)
        engine_path = r'C:\Users\POOJA\Downloads\stockfish-windows-x86-64-avx2\stockfish\stockfish-windows-x86-64-avx2.exe'
        engine = chess.engine.SimpleEngine.popen_uci(engine_path)
        result = engine.play(board, chess.engine.Limit(time=0.1))
        move = result.move
        board.push(move)
        self.fen = board.fen()
        self.save()
        engine.quit()
        return move.uci()

    def restart_game(self):
        self.fen = chess.STARTING_FEN
        self.winner = None
        self.save()
