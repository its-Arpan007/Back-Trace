import 'package:flutter/material.dart';

class AppColors {
  // Brand Primary & Accents (HSL Tailored)
  static const Color primary = Color(0xFF0F172A); // Deep Slate
  static const Color primaryLight = Color(0xFF1E293B);
  static const Color accentTeal = Color(0xFF14B8A6); // Vibrant Teal
  static const Color accentCyan = Color(0xFF06B6D4); // Cyan Glow
  static const Color accentIndigo = Color(0xFF6366F1); // Learning AI Indigo
  static const Color accentRose = Color(0xFFF43F5E); // Diagnostic Alert Rose

  // Dark Mode Surface & Backgrounds
  static const Color darkBackground = Color(0xFF090D16);
  static const Color darkSurface = Color(0xFF111827);
  static const Color darkCard = Color(0xFF1F2937);
  static const Color darkBorder = Color(0xFF374151);

  // Light Mode Surface & Backgrounds
  static const Color lightBackground = Color(0xFFF8FAFC);
  static const Color lightSurface = Color(0xFFFFFFFF);
  static const Color lightCard = Color(0xFFF1F5F9);
  static const Color lightBorder = Color(0xFFE2E8F0);

  // Text Colors
  static const Color textPrimaryDark = Color(0xFFF8FAFC);
  static const Color textSecondaryDark = Color(0xFF94A3B8);
  static const Color textPrimaryLight = Color(0xFF0F172A);
  static const Color textSecondaryLight = Color(0xFF64748B);

  // Status Colors
  static const Color success = Color(0xFF10B981);
  static const Color warning = Color(0xFFF59E0B);
  static const Color error = Color(0xFFEF4444);

  // Gradient Colors
  static const LinearGradient primaryGradient = LinearGradient(
    colors: [Color(0xFF0F172A), Color(0xFF1E1B4B)],
    begin: Alignment.topLeft,
    end: Alignment.bottomRight,
  );

  static const LinearGradient accentGradient = LinearGradient(
    colors: [Color(0xFF14B8A6), Color(0xFF6366F1)],
    begin: Alignment.topLeft,
    end: Alignment.bottomRight,
  );

  static const LinearGradient glassGradient = LinearGradient(
    colors: [
      Color(0x2B1F2937),
      Color(0x11111827),
    ],
    begin: Alignment.topLeft,
    end: Alignment.bottomRight,
  );
}
