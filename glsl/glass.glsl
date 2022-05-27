varying vec2 pos;
uniform sampler2D s_texture;
uniform float texture_width;
uniform float texture_height;

float random (in vec2 _st) {
    return fract(sin(dot(_st.xy, vec2(12.9898,78.233)))*43758.5453123);
}

void main() {
    float tx = pos.x;
    float ty = pos.y;
    float dx = 1.0 / texture_width;
    float dy = 1.0 / texture_height;


    vec4 v1 = texture2D( s_texture, vec2( tx, ty ) + vec2( -dx, -dy ) ).rgba;
    vec4 v2 = texture2D( s_texture, vec2( tx, ty ) + vec2( -dx, 0 ) ).rgba;
    vec4 v3 = texture2D( s_texture, vec2( tx, ty ) + vec2( -dx, dy ) ).rgba;
    vec4 v4 = texture2D( s_texture, vec2( tx, ty ) + vec2( 0, -dy ) ).rgba;
    vec4 v5 = texture2D( s_texture, vec2( tx, ty ) + vec2( 0 , 0 ) ).rgba;
    vec4 v6 = texture2D( s_texture, vec2( tx, ty ) + vec2( 0, dy ) ).rgba;
    vec4 v7 = texture2D( s_texture, vec2( tx, ty ) + vec2( dx, -dy ) ).rgba;
    vec4 v8 = texture2D( s_texture, vec2( tx, ty ) + vec2( dx, 0 ) ).rgba;
    vec4 v9 = texture2D( s_texture, vec2( tx, ty ) + vec2( dx, dy ) ).rgba;
    
    vec2 rand = vec2(tx, ty);
    int random = int(random(rand)*7.0+1.0);

    vec4 final_color;

    if (random == 1){
        final_color = vec4(v1.r, v1.g, v1.b, 1);
    }
    else if (random == 2){
        final_color = vec4(v2.r, v2.g, v2.b, 1);
    }
    else if (random == 3){
        final_color = vec4(v3.r, v3.g, v3.b, 1);
    }
    else if (random == 4){
        final_color = vec4(v4.r, v4.g, v4.b, 1);
    }
    else if (random == 5){
        final_color = vec4(v5.r, v5.g, v5.b, 1);
    }
    else if (random == 6){
        final_color = vec4(v6.r, v6.g, v6.b, 1);
    }
    else if (random == 7){
        final_color = vec4(v7.r, v7.g, v7.b, 1);
    }
    else if (random == 8){
        final_color = vec4(v8.r, v8.g, v8.b, 1);
    }
    
    gl_FragColor = clamp(abs(final_color), vec4(0,0,0,0), vec4(1,1,1,1));
}
